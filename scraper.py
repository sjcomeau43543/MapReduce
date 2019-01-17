#!/usr/bin/python
import requests, re, csv

def scrape(url, filename):
	# notes to console
	print "scraping", url, "..."
       
	# get the webpage data
	mas_txt = requests.get(url)

	title, date, author, description = '', '', '', ''
	all_four = 0
	# add the updated data
	for line in mas_txt.iter_lines():
		if "<h2 class=\'home-title\'>" in line:
			title = line.split('>')[1].split('<')[0]
			while (title.find('&') != -1) and (title.find(';') != -1):
				title = title[:title.find('&')] + title[title.find(';')+1:]
			print 'TITLE:', title
		elif "<i class=\'icon-font icon-calendar\'>" and "<i class=\'icon-font icon-user\'>" in line:
			date = line.split('>')[3].split('<')[0]
			print 'DATE:', date
			author = line.split('>')[6]
			print 'AUTHOR:', author
		elif "<div class=\'home-desc\'>" in line:
			description = line.split('>')[1].split('<')[0]
			while (description.find('&') != -1) and (description.find(';') != -1):
				description = description[:description.find('&')] + description[description.find(';')+1:]
			description = description.replace("...", "")
			print 'DESCRIPTION:', description
			all_four = 1
		
		if all_four:
			# open the file
			with open(filename, 'a') as csv_file:
				csv.writer(csv_file, delimiter=',', lineterminator='\n').writerow([title, date, author, description])
			all_four = 0

def main():
	filename = "thehackernews.csv"

	# make the output file
	open(filename, 'w+').close()
				
	# add the header lines
	with open(filename, 'a') as file:
		csv.writer(file, delimiter=',', lineterminator='\n').writerow(['Title', 'Date', 'Author', 'Description'])

	# scrape the data
	scrape("https://thehackernews.com/search?&max-results=20", filename)
	scrape("https://thehackernews.com/search?updated-max=2019-01-10T09:39:00%2B01:00&max-results=20&start=20&by-date=false", filename)
	scrape("https://thehackernews.com/search?updated-max=2018-12-19T09:43:00%2B01:00&max-results=20&start=40&by-date=false", filename)
	scrape("https://thehackernews.com/search?updated-max=2018-12-03T14:18:00%2B01:00&max-results=20&start=59&by-date=false", filename)
	scrape("https://thehackernews.com/search?updated-max=2018-11-15T16:09:00%2B01:00&max-results=20&start=78&by-date=false", filename)
	scrape("https://thehackernews.com/search?updated-max=2018-11-08T10:25:00%2B01:00&max-results=20&start=91&by-date=false", filename)
	scrape("https://thehackernews.com/search?updated-max=2018-10-19T16:12:00%2B02:00&max-results=20&start=110&by-date=false", filename)
	scrape("https://thehackernews.com/search?updated-max=2018-10-08T17:34:00%2B02:00&max-results=20&start=130&by-date=false", filename)
	scrape("https://thehackernews.com/search?updated-max=2018-09-27T21:20:00%2B02:00&max-results=20&start=146&by-date=false", filename)
	scrape("https://thehackernews.com/search?updated-max=2018-09-19T11:12:00%2B02:00&max-results=20&start=164&by-date=false", filename)
	scrape("https://thehackernews.com/search?updated-max=2018-09-06T15:08:00%2B02:00&max-results=20&start=184&by-date=false", filename)
	scrape("https://thehackernews.com/search?updated-max=2018-08-21T10:29:00%2B02:00&max-results=20&start=204&by-date=false", filename)
	scrape("https://thehackernews.com/search?updated-max=2018-08-08T12:33:00%2B02:00&max-results=20&start=222&by-date=false", filename)
	scrape("https://thehackernews.com/search?updated-max=2018-07-27T10:31:00%2B02:00&max-results=20&start=242&by-date=false", filename)
	scrape("https://thehackernews.com/search?updated-max=2018-07-15T09:49:00%2B02:00&max-results=20&start=262&by-date=false", filename)
	scrape("https://thehackernews.com/search?updated-max=2018-07-05T12:28:00%2B02:00&max-results=20&start=281&by-date=false", filename)
	scrape("https://thehackernews.com/search?updated-max=2018-06-26T13:53:00%2B02:00&max-results=20&start=299&by-date=false", filename)
	scrape("https://thehackernews.com/search?updated-max=2018-06-12T20:32:00%2B02:00&max-results=20&start=319&by-date=false", filename)
	scrape("https://thehackernews.com/search?updated-max=2018-06-05T11:47:00%2B02:00&max-results=20&start=339&by-date=false", filename)
	

if __name__ == '__main__':
	main()