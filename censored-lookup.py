import requests
import glob
import json
import os

file_location = os.path.join('summary-with-ip', '*site_stats.json')
filenames = glob.glob(file_location)
req = "https://geolocation-db.com/json/d802faa0-10bd-11ec-b2fe-47a0872c6708/"
output_dir = "censored-outputs"
 
for filename in filenames:
    censored_output = dict()  # format = website: anomaly_count, pass_count, category, ip
    print(filename)
    f = open(filename)
    json_object = json.load(f)
    for key, values in json_object.items():
        if values[0]/values[1] > .2:
            censored_output[key] = [values[2], values[3], "EMPT"]
            if values[3] != "0.0.0.0":
                try:
                    response = requests.get(req + values[3]).json()
                    censored_output[key][2] = response["country_code"]
                except:
                    print("exception!")
    output_loc = os.path.join(output_dir, os.path.basename(filename))
    with open(output_loc, "w") as outfile:
        json.dump(censored_output, outfile, indent=2)

