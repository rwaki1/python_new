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

print(files)