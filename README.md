# CensoredPlanetDataParser
A Data Parser for the Censored Planet security monitoring project

## Usage: extract-script.py or extract-script-resilient.py
* Clone this file to the directory you want to test in  
* add directories: raw, us, russia  
* put downloaded files in raw and then run

## Usage: Analyze.py
* Clone this file to the directory you want to analyze in.
* make sure you include the `site_cat.json` file in the same directory as Analyze.py
* add directories: samples, outputs
* copy `russia_april_data.txt` to `samples/` (replace `russia_april_data.txt` with whatever **single** file you are analyzing right now. **Do it for one country and one month at a time**)
* `python3 Analyze.py`

## Category Name Extraction
* Category name extraction file (global_csv.py)
* The source file (global.csv from OONI/CitizenLab)
* and the result json files (cat_names is category names; site_cat is the mapping of site to category)
both are easily parsable into python dicts
