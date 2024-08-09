//M. M. Kuttel 2024 mkuttel@gmail.com

// the main class, starts all threads
package barScheduling;

import java.io.FileWriter;
import java.io.IOException;
import java.util.concurrent.CountDownLatch;

public class SchedulingSimulation {
	static int noPatrons = 15; // number of customers - default value if not provided on command line
	static int sched = 0; // which scheduling algorithm, 0= FCFS

	static CountDownLatch startSignal;

	static Patron[] patrons; // array for customer threads
	static Barman Andre;
	static FileWriter writer;

	public static double totalWaitTime = 0.0;
	public static double totalResponseTime = 0.0;
	public static double totalTurnaroundTime = 0.0;

	public void writeToFile(String data) throws IOException {
		synchronized (writer) {
			writer.write(data);
		}
	}

	public static void main(String[] args) throws InterruptedException, IOException {

		// arg 1 = number of patrons to enter the room
		// arg 2 = scheduling algo, 0=FCFS and 1=SJF and 2=RR

		// deal with command line arguments if provided
		if (args.length == 1) {
			noPatrons = Integer.parseInt(args[0]); // total people to enter room
		} else if (args.length == 2) {
			noPatrons = Integer.parseInt(args[0]); // total people to enter room
			sched = Integer.parseInt(args[1]); // algorithm to use
		}

		writer = new FileWriter("output/data_" + Integer.toString(noPatrons) + "_" + Integer.toString(sched) + ".txt",
				false);
		Patron.fileW = writer;

		startSignal = new CountDownLatch(noPatrons + 2);// Barman and patrons and main method must be raeady

		// create barman
		Andre = new Barman(startSignal, sched);
		Andre.start();

		// create all the patrons, who all need access to Andre
		patrons = new Patron[noPatrons];
		for (int i = 0; i < noPatrons; i++) {
			patrons[i] = new Patron(i, startSignal, Andre);
			patrons[i].start();
		}

		System.out.println("------Andre the Barman Scheduling Simulation------");
		System.out.println("-------------- with " + Integer.toString(noPatrons) + " patrons---------------");

		long startTime = System.currentTimeMillis();
		startSignal.countDown(); // main method ready

		// wait till all patrons done, otherwise race condition on the file closing!
		for (int i = 0; i < noPatrons; i++) {
			patrons[i].join();
		}

		System.out.println("------Waiting for Andre------");
		Andre.interrupt(); // tell Andre to close up
		Andre.join(); // wait till he has

		long totalTime = System.currentTimeMillis() - startTime;
		double throughput = (double) noPatrons / totalTime;

		// other metrics are recorded in Patron.java

		synchronized (Patron.fileW) {
			Patron.fileW.write(String.format("TotalTime:%d\nThroughput:%.10f\n", totalTime, throughput));
			Patron.fileW.write(String.format("AvgTurnaroundTime:%.2f\nAvgWaitTime:%.2f\nAvgResponseTime:%.2f",
					totalTurnaroundTime / noPatrons, totalWaitTime / noPatrons, totalResponseTime / noPatrons));
		}

		writer.close(); // all done, can close file
		System.out.println("------Bar closed------");

		System.out.println(String.format("\n--- Statistics ---\n\nTotal Time: %d ms", totalTime));
		System.out.printf("Throughput: %.10f patrons/ms\n", throughput);
		System.out.printf(
				"Average Turnaround Time: %.2f ms\nAverage Wait Time: %.2f ms\nAverage Response Time: %.2f ms\n\n--- Done ---\n\n",
				totalTurnaroundTime / noPatrons, totalWaitTime / noPatrons, totalResponseTime / noPatrons);
	}

}
