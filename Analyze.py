#!/usr/bin/env python
# coding: utf-8

# In[21]:


# Analysis of blocking in the Russian Federation

import os, glob, tarfile, json, timeit

from typing import List

DEBUG = True

file_location = os.path.join('samples', '*.txt')
filenames = glob.glob(file_location)
print(filenames)

site_cat_filename = 'site_cat.json'
categories = dict()
with open(site_cat_filename, 'r') as sc_file:
    categories = json.load(sc_file)


# this will conglomerate all the stats in the filename list `filenames` into two dicts!
# if your file is an entire month's worth of data, call this function with the parameter ['filename'] instead of just 'filename'
def extract_stats(filenames: List[str], categories: dict):
    not_printed = True

    website_stats = dict()  # format= website : anomaly_count, pass_count, category
    category_stats = dict()  # format= category : anomaly_count, pass_count

    for filename in filenames:
        with open(filename, 'r') as file:
            # each line of the file is parsable into a json object
            progress_counter = 0
            for line in file:
                if progress_counter % 100000 == 0:
                    print('.', end='')
                progress_counter += 1
                data_line = json.loads(line)
                anomaly = data_line['anomaly']
                url = data_line['response'][0]['url']
                category = categories[url] if url in categories else 'other'
                if not_printed:
                    print(json.dumps(data_line, indent=2))
                    not_printed = False
                    print(url, category, anomaly)

                anom_ct = 1 if anomaly == True else 0
                pass_ct = 1 if anomaly == False else 0
                if url not in website_stats:
                    website_stats[url] = [anom_ct, pass_ct, category]
                else:
                    website_stats[url][0] += anom_ct
                    website_stats[url][1] += pass_ct

                if category not in category_stats:
                    category_stats[category] = [anom_ct, pass_ct]
                else:
                    category_stats[category][0] += anom_ct
                    category_stats[category][1] += pass_ct
    return website_stats, category_stats

starttime = timeit.default_timer()
site_stats, cat_stats = extract_stats(filenames, categories)
endtime = timeit.default_timer()
print("Stat extraction took", endtime - starttime)


print(site_stats)
print(cat_stats)


# In[24]:


# save the output dicts to json files

output_dir = 'outputs'
output_fileloc_site_stats = os.path.join(output_dir, 'site_stats.json')
output_fileloc_cat_stats = os.path.join(output_dir, 'cat_stats.json')

with open(output_fileloc_site_stats, 'w') as ssfile, open(output_fileloc_cat_stats, 'w') as csfile:
    json.dump(site_stats, ssfile, indent=2)
    json.dump(cat_stats, csfile, indent=2)
print('done')


# In[ ]:





# ## Notes from Stackoverflow
#
#
# ### File iteration tips
#
# https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list/35622867#35622867
#
# 163
#
# You could simply do the following, as has been suggested:
# ```
# with open('/your/path/file') as f:
#     my_lines = f.readlines()
# ```
# Note that this approach has 2 downsides:
#
# 1) You store all the lines in memory. In the general case, this is a very bad idea. The file could be very large, and you could run out of memory. Even if it's not large, it is simply a waste of memory.
#
# 2) This does not allow processing of each line as you read them. So if you process your lines after this, it is not efficient (requires two passes rather than one).
#
# A better approach for the general case would be the following:
# ```
# with open('/your/path/file') as f:
#     for line in f:
#         process(line)
# ```
# Where you define your process function any way you want. For example:
# ```
# def process(line):
#     if 'save the world' in line.lower():
#          superman.save_the_world()
# ```
# (The implementation of the Superman class is left as an exercise for you).
#
# This will work nicely for any file size and you go through your file in just 1 pass. This is typically how generic parsers will work.
#
# ### with-as open file statement closure
#
# https://stackoverflow.com/questions/21275836/if-youre-opening-a-file-using-the-with-statement-do-you-still-need-to-close
#
# The answer to your immediate question is "No". The with block ensures that the file will be closed when control leaves the block, for whatever reason that happens, including exceptions (well, excluding someone yanking the power cord to your computer and some other rare events).
