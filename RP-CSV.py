#Creating a script that takes a list of running processes and stores it on a CSV file called processes.csv

# Import a list of all the modules to be used in the script:
# The Python OS module allows one to interact with their operating system 
# The Python psutil Module allows one to retrieve information on running processes and system utilization (CPU, memory, disks, network, sensors)
# The Python CSV module provides functionality for reading and writing data in the CSV (Comma-Separated Values) format. Usually, this data is structured in a table much like an Excel spreadsheet
import os
import psutil
import csv

# Created an empty list that will get all running processes
processes = []

# Used a For Loop to iterate through all running processes and filter it to retrieve the Process ID, Name, Executable path, CPU Percentage, and Memory percentage
# Used a try and except block to catch any errors in retrieving the processes using psutil

for proc in psutil.process_iter(attrs=['pid', 'name', 'exe', 'cpu_percent', 'memory_percent']):
    try:
        process = proc.info
        processes.append(process)
    except (psutil.NoSuchProcess,  psutil.AccessDenied):
        pass

# Define the CSV file name
csv_filename = "processes.csv"

# Define the headers for the CSV file
csv_headers = ["Process ID", "Name", "Executable Path", "CPU Usage", "Memory Usage"]

# Open the CSV file in write mode, formatted to newline.for every word enclosed in '' will appear on a new line for better user experience and readability 
with open(csv_filename, mode='w', newline='') as csv_file:
  # used csv.writer to write the processes to the csv file
    writer = csv.writer(csv_file)
    writer.writerow(csv_headers)  # Write the headers to the CSV file

    # Iterate through the list of processes and write their information to the CSV file using a for loop to iterate through  and print the process attributes 1 by 1 , row by row
    for process in processes:
      # writer.writerow is used to create all the comma-separated values that would be present in the CSV file
        writer.writerow([
            process['pid'],
            process['name'],
            process['exe'],
            process['cpu_percent'],
            process['memory_info']
        ])
# When the entire script is done, a message is printed telling me that the CSV file has been successfully created
print(f"CSV file '{csv_filename}' has been successfully created!")
