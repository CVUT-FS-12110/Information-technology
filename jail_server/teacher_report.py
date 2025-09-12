#!/usr/bin/python3
import os
from glob import glob

# Folder containing student home directories
students_base = "/home"

# Output report
report = []

# Iterate over all student directories
for student_dir in glob(os.path.join(students_base, "student*")):
    log_file = os.path.join(student_dir, "student_runs.log")
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            lines = f.readlines()
            for line in lines:
                report.append(line.strip())

# Print consolidated report
if report:
    print("=== Students Runs Report ===")
    for entry in sorted(report):
        print(entry)
else:
    print("No student runs found.")
