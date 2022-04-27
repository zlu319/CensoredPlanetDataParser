import requests
import glob
import json
import os
import math 

inputdir = 'summary-with-ip'
file_location = os.path.join(inputdir, '*site_stats.json')
filenames = glob.glob(file_location)
req = "https://geolocation-db.com/json/d802faa0-10bd-11ec-b2fe-47a0872c6708/"
output_dir = "histogram-outputs"
 
for filename in filenames:
    count = [0] * 21  # format = website: anomaly_count, pass_count, category, ip
    print(filename)
    f = open(filename)
    json_object = json.load(f)
    for key, values in json_object.items():
        ratio = values[0]/(values[1]+values[0])
        index = math.floor(ratio * 20)
        count[index] += 1
    temp = 0
    for i in range(0,21):
        print("{:.2f}, {}".format(temp, count[i]))
        temp += .05
