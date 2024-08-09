import decimal
import numpy as np
import matplotlib.pyplot as plt
import sys

filename = sys.argv[1]

with open(filename + ".txt", "r") as file:
    data = file.readlines()

id = []
tt = []
wt = []
rt = []

for entry in data[:-2]: #  skip last two lines
    vals = entry.split(",")
    id.append(vals[0])
    tt.append(int(vals[1]))
    wt.append(int(vals[2]))
    rt.append(int(vals[3]))

file.close()

# Prepare data for plotting
x = np.arange(len(id))  # Create x values for the bars
width = 0.25  # Width of the bars

# Plot stacked histogram
fig, ax = plt.subplots()
bars_tt = ax.bar(x - width, tt, width, label='Turnaround Time')
bars_wt = ax.bar(x, wt, width, label='Waiting Time')
bars_rt = ax.bar(x + width, rt, width, label='Response Time')

# Add labels, title, and legend
params = filename.split('_')
alg = '-1'
if (params[2] == "0"):
    alg = 'FCFS'
elif (params[2] == "1"):
    alg = 'SJF'
elif (params[2] == "2"):
    alg = 'RR'

throughput = data[len(data) - 1]
throughput = throughput[11:]

title = 'Time Metrics - ' + params[1] + ' Patrons, ' + alg + '\n[Throughput: ' +  str(round(1000*float(throughput.replace(',','.')),3)) +' patrons/sec]'

ax.set_xlabel('Patron ID')
ax.set_ylabel('Time (ms)')
ax.set_title(title)
ax.set_xticks(x)
ax.set_xticklabels(id)
ax.legend()

# Calculate and print averages
avg_tt = np.mean(tt)
avg_wt = np.mean(wt)
avg_rt = np.mean(rt)
ax.axhline(avg_tt, color='blue', linestyle='--', label=f'Average Turnaround Time: {avg_tt:.2f}')
ax.axhline(avg_wt, color='orange', linestyle='--', label=f'Average Waiting Time: {avg_wt:.2f}')
ax.axhline(avg_rt, color='green', linestyle='--', label=f'Average Response Time: {avg_rt:.2f}')
print("Average Turnaround Time:", avg_tt)
print("Average Waiting Time:", avg_wt)
print("Average Response Time:", avg_rt)

ax.legend()

#plt.savefig(filename + '.png')

print("Graph saved to "  + filename + ".png")

plt.show()
