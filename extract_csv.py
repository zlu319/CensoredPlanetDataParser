#!/bin/python3

# OONI/CitizenLab Global Categories

import csv
import json
import os
import glob

from typing import List
from urllib.parse import urlparse

file_location = os.path.join('blocklists', '*.csv')
filenames = glob.glob(file_location)
print(filenames)

# give URL to category mapping
def parse_csv_url(filenames: List[str]):
    websites_and_categories = dict()

    for filename in filenames:
        blocklist = open(filename, 'r')
        reader = csv.DictReader(blocklist, skipinitialspace=True)
        for row in reader:
            url = row['url']
            cat_code = row['category_code']
            websites_and_categories[url] = cat_code

        blocklist.close()
    return websites_and_categories


# give domain to category mapping
def parse_csv(filenames: List[str]):
    websites_and_categories = dict()

    for filename in filenames:
        blocklist = open(filename, 'r')
        reader = csv.DictReader(blocklist, skipinitialspace=True)
        for row in reader:
            url = row['url']
            domain = urlparse(url).netloc
            cat_code = row['category_code']
            websites_and_categories[domain] = cat_code

        blocklist.close()
    return websites_and_categories



sc = parse_csv(filenames)

with open('site_cat.json', 'w') as outfile:
    json.dump(sc, outfile, indent=2)


