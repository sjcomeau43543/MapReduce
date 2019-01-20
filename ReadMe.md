# MapReduce for thehackernews.com

## Description

### scraper.py
The scraper script will reach out to thehackernews.com starting from Jan 2019 and going back until June 2018 collecting the title, date, author, and shortened description of the article. It will store this information in a CSV and also print it out to the console during execution based on different input parameters.

### mapper.py
The mapper script will read from stdin to produce a 'dictionary' of words and the count of the word per line. 'Dictionary' meaning that it will print the results to stdout but will not actually store a dictionary of items.

### reducer.py
The reducer script will read from stdin to simplify the dictionary given from the mapper script. Given a sorted dictionary, it will check to see if the next word is the same as the previous word and combine those results so the word count is updated. It will then print these results to stdout.

## Using this
To incorporate all of these components the suggested use is below.
1. Run the scraper script to collect the data `python scraper.py --title --description'
2. Run the mapper script, sort the results, and run the reducer script
2a. 

## Integrating into Amazon S3 and EMR

## Sample output

| Word | Count |
|-------|-------|
| android	| 49 |
| androidapk |	1 |
| announced	| 10 |
| announcement |	1 |
| announcements |	1 |
| announces	| 2 |
| another	| 22 |
| answering	| 1 |
| anticipated |	1 |
| antiencryption |	1 |
| antimalware |	2 |
| antipiracy |	2 |
| antispoofing |	2 |
| antitrust |	2 |
| antivirus |	3 |
