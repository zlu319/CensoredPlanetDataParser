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

ratio_threshold = 1 / 6  # corresponds to the cutoff of 0.2 we had for values[0] / values[1]

total_num_censored = 0
total_not_censored = 0

for filename in filenames:
    count = [0] * 21  # format = website: anomaly_count, pass_count, category, ip
    print(filename)
    f = open(filename)
    json_object = json.load(f)

    num_censored = 0
    num_total = 0
    num_not_censored = 0

    for key, values in json_object.items():
        ratio = values[0]/(values[1]+values[0])
        index = math.floor(ratio * 20)
        count[index] += 1
        if ratio > ratio_threshold:  # over 1/6 of accesses were anomalous
            num_censored += 1
        else:
            num_not_censored += 1
        num_total += 1

    temp = 0
    for i in range(0,21):
        print("{:.2f}, {}".format(temp, count[i]))
        temp += .05
    print("Num censored: {}, Num not censored {}, Num total {}\n\n".format(num_censored, num_not_censored, num_total))
    total_num_censored += num_censored
    total_not_censored += num_not_censored

print('*' * 10, " IN TOTAL FOR ALL FILES IN DIR ", '*' * 10)
print("Num censored: {}, Num not censored {}".format(total_num_censored, total_not_censored))

