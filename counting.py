import os, json, glob

file_location = os.path.join('censored-outputs', '*site_stats.json')
filenames = glob.glob(file_location)

for f in filenames:
    print(f)
    category_stats = dict() 
    src_stats = dict()
    src_stats["null"] = [0]
    filen = open(f)
    json_obj = json.load(filen)
    for key, value in json_obj.items():
        if value[0] not in category_stats:
            category_stats[value[0]] = [1]
        else:
            category_stats[value[0]][0] += 1
        if value[2] is None:
            src_stats["null"][0] += 1
        else:
            if value[2] not in src_stats:
                src_stats[value[2]] = [1]
            else:
                src_stats[value[2]][0] += 1

    print(category_stats)
    print("\n")
    print(src_stats)

