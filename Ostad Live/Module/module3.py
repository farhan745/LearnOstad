# Subprocess
# hashlib
# CSV
import subprocess as sub

result = sub.run(
    ["python", "--version"],
    capture_output=True,
    text=True,
)
print(result.stdout)

import hashlib

# Hashing
password = b"Abcd123"
has_obj = hashlib.sha256(password)
print(has_obj.hexdigest)

import csv

# csv

with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 25, "New York"])
