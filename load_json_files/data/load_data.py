#!/usr/bin/env python3

# Place this Python script in your working directory when you have JSON files in a subdirectory.
# To run the script via command line: "python3 json-to-csv-exporter.py"

import json
import glob
from datetime import datetime, time
import csv

# Place your JSON data in a directory named 'data/'
src = "/load_json_files/data"
#dateTimeStamp = time.strftime('%y-%m-%d-%H-%M-%S')
date = datetime.now()
data = []

# Change the glob if you want to only look through files with specific names
files = glob.glob('D:/Python/load_json_files/data/*.json', recursive=True)

# Loop through files

for single_file in files:
  with open(single_file, 'r') as f:
    json_file = json.load(f)
    data.append([
      json_file['firstName'],
      json_file['lastName'],
      json_file['gender'],
      json_file['age'],
      json_file['address']['streetAddress'],
      json_file['address']['city'],
      json_file['address']['state'],
      json_file['address']['postalCode'],
      json_file['phoneNumbers'][0]
      #json_file['phoneNumbers'][int('number')]

  ])

# Sort the data
data.sort()
print(data)
# Add headers
print(type(files))

data.insert(0, ['First Name', 'Lat Name', 'Genda', 'Age', 'street Address', 'City', 'State', 'Post Code', 'Type','Number','Date'])

# Export to CSV.
# Add the date to the file name to avoid overwriting it each time.
with open(   '.csv', "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("Updated CSV")