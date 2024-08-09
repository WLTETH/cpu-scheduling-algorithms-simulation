import os
import csv
import numpy as np

def calculate_average_metrics(directory):
    files = [file for file in os.listdir(directory) if file.endswith('.csv')]
    if not files:
        print("No CSV files found in the directory:", directory)
        return

    total_times = []
    throughputs = []
    avg_turnaround_times = []
    avg_wait_times = []
    avg_response_times = []

    for file in files:
        with open(os.path.join(directory, file), 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row:
                    if row[0] == 'TotalTime':
                        total_times.append(float(row[1].replace(',', '.')))  # Replace comma with dot
                    elif row[0] == 'Throughput':
                        throughputs.append(float(row[1].replace(',', '.')))  # Replace comma with dot
                    elif row[0] == 'AvgTurnaroundTime':
                        avg_turnaround_times.append(float(row[1].replace(',', '.')))  # Replace comma with dot
                    elif row[0] == 'AvgWaitTime':
                        avg_wait_times.append(float(row[1].replace(',', '.')))  # Replace comma with dot
                    elif row[0] == 'AvgResponseTime':
                        avg_response_times.append(float(row[1].replace(',', '.')))  # Replace comma with dot

    # Calculate averages
    avg_total_time = np.mean(total_times)
    avg_throughput = np.mean(throughputs)
    avg_turnaround_time = np.mean(avg_turnaround_times)
    avg_wait_time = np.mean(avg_wait_times)
    avg_response_time = np.mean(avg_response_times)

    # Calculate predictabilities (variances)
    var_total_time = np.var(total_times)
    var_throughput = np.var(throughputs)
    var_turnaround_time = np.var(avg_turnaround_times)
    var_wait_time = np.var(avg_wait_times)
    var_response_time = np.var(avg_response_times)

    return {
        'AvgTotalTime': avg_total_time,
        'AvgThroughput': avg_throughput,
        'AvgTurnaroundTime': avg_turnaround_time,
        'AvgWaitTime': avg_wait_time,
        'AvgResponseTime': avg_response_time,
        'Predictability_TotalTime': var_total_time,
        'Predictability_Throughput': var_throughput,
        'Predictability_TurnaroundTime': var_turnaround_time,
        'Predictability_WaitTime': var_wait_time,
        'Predictability_ResponseTime': var_response_time
    }

def write_average_metrics(average_metrics, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Metric', 'Value'])
        for metric, value in average_metrics.items():
            writer.writerow([metric, value])

def main():
    input_directory = os.getcwd()
    output_file = 'average_metrics.csv'

    average_metrics = calculate_average_metrics(input_directory)
    write_average_metrics(average_metrics, output_file)
    print("Averaged metrics CSV file saved as:", output_file)

if __name__ == "__main__":
    main()