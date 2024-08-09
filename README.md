# CPU Scheduling Algorithms Simulation
A Java simulation of popular CPU scheduling algorithms using an analogy of a Andre the Barman (The CPU) serving bar patrons (jobs)

## The following algorithms can be simulated:
#### First Come First Served (FCFS)
#### Shortest Job First (SJF)
#### Round Robin (RR)

### To run the simulation, run the following command in the directory of the Makefile

```bash
  > make run ARGS="<num_patrons> <0/1/2, 0=FCFS 1=SJF 2=RR"
```

#### For example, to run a SJF simulation for 10 patrons:

```bash
  > make run ARGS="10 1"
``` 

## Findings
![image](https://github.com/user-attachments/assets/2624e04c-0320-41dc-a946-ac28f5b6d089)
![image](https://github.com/user-attachments/assets/77402f63-2727-4b73-8ee1-571d7f377fd3)

## Recommendation
Based on the metrics I have collected I would recommend the Shortest Job First (SJF) algorithm. It has the best metrics in all areas bar throughput and is relatively predictable.
