# CensoredPlanetDataParser
A Data Parser for the Censored Planet security monitoring project: Satellite Dataset Only

## Pipeline Stage 1
### Usage: extract-script.py or extract-script-resilient.py
* Clone this file to the directory you want to test in  
* add directories: raw, us, russia  
* put downloaded files in raw and then run


## Pipeline Stage 2
### Usage: Analyze.py (use Analyze-with-ip.py instead to use the next stage in the pipeline)
* Clone this file to the directory you want to analyze in.
* make sure you include the `site_cat.json` file in the same directory as Analyze.py
* add directories: samples, outputs
* copy `russia_april_data.txt` to `samples/` (replace `russia_april_data.txt` with whatever **single** file you are analyzing right now. **Do it for one country and one month at a time**)
* `python3 Analyze.py`

Note `histogram.py` can be run on the results of `Analyze-with-ip.py`. This tool will calculate the statistics of censored and uncensored websites.

## Pipeline Stage 3
### Usage: censored-lookup.py (don't use the limited version; we will lose API accesses)
* Clone this file into the directory you want to analyze on
* add directories: `summary-with-ip` (for input data) and `censored-outputs` (for output data)
* Rename the output files from the `outputs` directory in the previous pipeline stage (Analyze-with-ip.py) to the following format:
    `month-country-site_stats.json`. You will only need the site_stats.json files
* Copy all the `*site_stats.json` files to `summary-with-ip` (for input data).
* `python3 censored-lookup.py`
* Results of IP geolocation will be in `censored-outputs`.

## Statistical Analysis Tools
* `fisher-test.py` is an interactive python tool to help you run [Fisher's Exact Test](https://en.wikipedia.org/wiki/Fisher%27s_exact_test) on large numbers that Excel/GNUmeric/LibreOffice-Calc/Google-Sheets disallows in the `COMB()` or `FACT()` functions.

## Pipeline Stage 0: Category Name Extraction (the output of this stage, site_cat.json, is important for stages 2 and 3)

### global.csv (only for initial testing, not used!)
* Category name extraction file `global_csv.py`
* The source file (`global.csv` from OONI/CitizenLab)
* and the result json files (cat_names is category names; site_cat is the mapping of site to category)
both are easily parsable into python dicts


### all .csv files from OONI/CitizenLab (the mapping of site -> category that we actually use)
* Category name extraction file `extract_csv.py`
* The source files (all site -> category mapping `.csv` files from OONI/CitizenLab)
* and the result json files (`cat_names.json` is category names; `site_cat.json` is the mapping of site to category for all files)
both are easily parsable into python dicts

The `site_cat.json` file used here is the important output used for stages 2 and 3, and included in the root of the github repo.
