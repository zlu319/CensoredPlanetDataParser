#!/bin/python3

# OONI/CitizenLab Global Categories

import csv
import json


def parse_csv(filename: str):
    websites_and_categories = dict()
    category_code_explanations = dict()

    blocklist = open(filename, 'r')
    reader = csv.DictReader(blocklist, skipinitialspace=True)
    for row in reader:
        url = row['url']
        cat_code = row['category_code']
        cat_description = row['category_description']
        websites_and_categories[url] = cat_code
        category_code_explanations[cat_code] = cat_description

    blocklist.close()
    return websites_and_categories, category_code_explanations

fn = 'global.csv'

sc, cn = parse_csv(fn)

with open('site_cat.json', 'w') as outfile:
    json.dump(sc, outfile, indent=2)

with open('cat_names.json', 'w') as of:
    json.dump(cn, of, indent=2)

