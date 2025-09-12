#!/usr/bin/python3
import sys
import datetime
import os

# Ensure exactly one argument is provided
if len(sys.argv) != 2:
    print("Usage: runner <your_name>")
    sys.exit(1)

name = sys.argv[1]

# Log file inside student's home folder
log_file = os.path.expanduser("~/student_runs.log")

# Print a greeting
print(f"Hello, {name}! Running your exercise...")

# Append timestamp and name to log file
with open(log_file, "a") as f:
    f.write(f"{name} ran the script at {datetime.datetime.now()}\n")

print(f"Run logged in {log_file}")