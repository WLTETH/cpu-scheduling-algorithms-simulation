package barScheduling;

import java.util.Comparator;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.concurrent.PriorityBlockingQueue;

/*
 Barman Thread class.
 */

public class Barman extends Thread {

	private CountDownLatch startSignal;

	private BlockingQueue<DrinkOrder> orderQueue;

	private PriorityBlockingQueue<DrinkOrder> sjfOrderQueue;

	private LinkedBlockingQueue<DrinkOrder> rrOrderQueue;

	private int algorithm;

	Barman(CountDownLatch startSignal, int schedAlg) {

		algorithm = schedAlg;

		if (schedAlg == 0) {
			this.orderQueue = new LinkedBlockingQueue<>();
		} else if (schedAlg == 1) {
			Comparator<DrinkOrder> drinkComparator = Comparator.comparingInt(DrinkOrder::getExecutionTime);
			this.sjfOrderQueue = new PriorityBlockingQueue<>(SchedulingSimulation.noPatrons, drinkComparator);
		} else if (schedAlg == 2) {
			this.rrOrderQueue = new LinkedBlockingQueue<>();
		}

		this.startSignal = startSignal;
	}

	public void placeDrinkOrder(DrinkOrder order) throws InterruptedException {
		if (algorithm == 0)
			orderQueue.put(order);
		else if (algorithm == 1)
			sjfOrderQueue.add(order);
		else if (algorithm == 2)
			rrOrderQueue.put(order);
	}

	public void run() {
		try {
			DrinkOrder nextOrder;

			startSignal.countDown(); // barman ready
			startSignal.await(); // check latch - don't start until told to do so

			// provided FCFS algorithm
			if (algorithm == 0) {
				while (true) {
					nextOrder = orderQueue.take();
					System.out.println("---Barman preparing order for patron " + nextOrder.toString());
					sleep(nextOrder.getExecutionTime()); // processing order
					System.out.println("---Barman has made order for patron " + nextOrder.toString());
					nextOrder.orderDone();
				}

				// SJF algorithm
				// uses a priority blocking queue with a comparator based on the execution time
				// of drink orders
			} else if (algorithm == 1) {

				while (true) {
					nextOrder = sjfOrderQueue.take();
					System.out.println("---Barman preparing order for patron " + nextOrder.toString());
					sleep(nextOrder.getExecutionTime()); // processing order
					System.out.println("---Barman has made order for patron " + nextOrder.toString());
					nextOrder.orderDone();
				}

				// RR algorithm
				// uses a linked blocking queue (FCFS queue) but adds incomplete drinks back to
				// the end of the queue
			} else if (algorithm == 2) {
				int quantum = 120; // 80% rule

				while (true) {

					nextOrder = rrOrderQueue.take();
					System.out.println("---Barman preparing order for patron " + nextOrder.toString());

					long executionTime = nextOrder.getExecutionTime();

					long remainingTime = quantum - executionTime; // calculate the difference between the quantum and
																	// the execution time

					if (remainingTime < 0) { // if the execution time is longer than the quantum
						sleep(quantum);
						remainingTime = Math.abs(remainingTime); // how much the execution time was longer than the
																	// quantum (need positive value)
						nextOrder.setExecutionTime((int) remainingTime); // set the execution time of the current order
																			// to the time that is left over
						rrOrderQueue.put(nextOrder);
						System.out.println("---Barman is delaying order for patron " + nextOrder.toString());
					} else { // sleep for execution time then mark as done so that next order can be
								// processed
						sleep(executionTime);
						System.out.println("---Barman has made order for patron " + nextOrder.toString());
						nextOrder.orderDone();
					}

				}

			}

		} catch (InterruptedException e1) {
			System.out.println("---Barman is packing up ");
		}
	}
}
