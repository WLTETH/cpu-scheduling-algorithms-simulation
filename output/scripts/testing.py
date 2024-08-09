import csv
import os

def process_text_file(file_path):
    data = []
    headings = ['ID', 'TurnaroundTime', 'WaitingTime', 'ResponseTime']  # Define headings
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith('TotalTime:'):
                total_time = line.split(':')[1].strip()
                data.append(['TotalTime', total_time])
            elif line.startswith('Throughput:'):
                throughput = line.split(':')[1].strip()
                data.append(['Throughput', throughput])
            elif line.startswith('AvgTurnaroundTime:'):
                avg_turnaround_time = line.split(':')[1].strip()
                data.append(['AvgTurnaroundTime', avg_turnaround_time])
            elif line.startswith('AvgWaitTime:'):
                avg_wait_time = line.split(':')[1].strip()
                data.append(['AvgWaitTime', avg_wait_time])
            elif line.startswith('AvgResponseTime:'):
                avg_response_time = line.split(':')[1].strip()
                data.append(['AvgResponseTime', avg_response_time])
            else:
                # Splitting the line by comma and adding to the data
                values = line.strip().split(',')
                data.append(values)
    # Insert headings at the beginning of the data
    data.insert(0, headings)
    return data

def save_to_csv(data, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

def main():
    input_directory = os.getcwd()  # Get the current working directory
    output_directory = input_directory  # Output directory same as input directory

    for filename in os.listdir(input_directory):
        if filename.endswith('.txt'):
            input_file_path = os.path.join(input_directory, filename)
            output_file_path = os.path.join(output_directory, filename.split('.')[0] + '.csv')
            
            # Process text file
            data = process_text_file(input_file_path)

            # Save data to CSV
            save_to_csv(data, output_file_path)

            print("Done")

if __name__ == "__main__":
    main()
