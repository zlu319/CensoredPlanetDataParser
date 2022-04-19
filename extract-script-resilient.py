import os
import glob
import tarfile
import json

results_substring = "results.json"

file_location = os.path.join('raw', '*.tar.gz')
filenames = glob.glob(file_location)
print(filenames)

def tardir(path, tar_name):
    with tarfile.open(tar_name, "w:gz") as tar_handle:
        for root, dirs, files in os.walk(path):
            for file in files:
                tar_handle.add(os.path.join(root, file))

def getmonth(filename):
    if "2022-01" in filename:
        return "january"
    if "2022-02" in filename:
        return "february"
    if "2022-03" in filename:
        return "march"
    if "2022-04" in filename:
        return "april"
    return "month"

for f in filenames:
    month = getmonth(f)
    with open('us/' + 'us_' + month + '_data.txt', 'a') as us_data, open('russia/' + 'russia_' + month + '_data.txt', 'a') as russia_data:
        try:
            tar = tarfile.open(f, "r:gz")
            for member in tar.getmembers():
                if results_substring in member.name:
                    print(member.name)
                    data = tar.extractfile(member)
                    for line in data:
                        data_line = json.loads(line)
                        if data_line['location']['country_name'] == 'United States':
                            us_data.write(line.decode())
                        if data_line['location']['country_name'] == 'Russia':
                            russia_data.write(line.decode())
            tar.close()
        except:
            print('an error occured')
            tar.close()
    us_data.close()
    russia_data.close()

tardir('./us', 'us.tar.gz')
tardir('./russia', 'russia.tar.gz')

