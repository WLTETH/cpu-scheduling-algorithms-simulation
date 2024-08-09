import os
from datetime import datetime
import shutil

# Get the current time in HH_MM format
current_time = datetime.now().strftime("%Hh_%Mm")

# List all files in the current directory
files = os.listdir()

# Iterate through each file
for file in files:
    # Check if the file is a .txt file
    if file.endswith('.txt'):
        # Split the file name and extension
        name, ext = os.path.splitext(file)
        # Split the file name by "_"
        name_parts = name.split("_")
        # Append the current time to the file name
        new_name = f"{name}_{current_time}{ext}"
        # Rename the file
        os.rename(file, new_name)
        print(f"Renamed '{file}' to '{new_name}'")

        if (name_parts[2] == "0"): #FCFS
            sub_folder = name_parts[1] + "patrons"
            dest_folder = "0 (FCFS)/" + sub_folder
            shutil.move(new_name, dest_folder)
            print(f"Moved '{new_name}' to folder '0 (FCFS)'")
        if (name_parts[2] == "1"): #FCFS
            sub_folder = name_parts[1] + "patrons"
            dest_folder = "1 (SJF)/" + sub_folder
            shutil.move(new_name, dest_folder)
            print(f"Moved '{new_name}' to folder '1 (SJF)'")
        if (name_parts[2] == "2"): #FCFS
            sub_folder = name_parts[1] + "patrons"
            dest_folder = "2 (RR)/" + sub_folder
            shutil.move(new_name, dest_folder)
            print(f"Moved '{new_name}' to folder '2 (RR)'")
