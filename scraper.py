#!/usr/bin/python
import requests, re, csv, sys, argparse

def standardize(string):
	punctuations = '''!()-[];:'"\,<>./?@#$%^&*_~'''

	cleaned = ''
	for char in string:
		if char not in punctuations:
			cleaned = cleaned + char
	
	return cleaned.lower()

def scrape(url, filename, print_title, print_datetime, print_author, print_description):
	# get the webpage data
	mas_txt = requests.get(url)

	title, date, author, description = '', '', '', ''
	all_four = 0
	row = []
	
	# add the updated data
	for line in mas_txt.iter_lines():
		if "<h2 class=\'home-title\'>" in line:
			title = line.split('>')[1].split('<')[0]
			while (title.find('&') != -1) and (title.find(';') != -1):
				title = title[:title.find('&')] + title[title.find(';')+1:]
			title = standardize(title)
			if print_title: 
				print 'TITLE:', title
				row.append(title)
		elif "<i class=\'icon-font icon-calendar\'>" and "<i class=\'icon-font icon-user\'>" in line:
			date = line.split('>')[3].split('<')[0]
			if print_datetime: 
				print 'DATE:', date
				row.append(date)
			author = line.split('>')[6]
			if print_author: 
				print 'AUTHOR:', author
				row.append(author)
		elif "<div class=\'home-desc\'>" in line:
			description = line.split('>')[1].split('<')[0]
			while (description.find('&') != -1) and (description.find(';') != -1):
				description = description[:description.find('&')] + description[description.find(';')+1:]
			description = standardize(description)
			if print_description: 
				print 'DESCRIPTION:', description
				row.append(description)
			all_four = 1
		
		if all_four:
			# open the file
			with open(filename, 'a') as csv_file:
				csv.writer(csv_file, delimiter=',', lineterminator='\n').writerow(row)
			all_four = 0
			row = []

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--author', action='store_true', help='print the author')
	parser.add_argument('--title', action='store_true', help='print the title')
	parser.add_argument('--description', action='store_true', help='print the description')
	parser.add_argument('--datetime', action='store_true', help='print the datetime')

	args = parser.parse_args()
	print args
	

	filename = "thehackernews.csv"

	# make the output file
	open(filename, 'w+').close()
	
	title_row = []
	if args.title:
		title_row.append('Title')
	if args.author:
		title_row.append('Author')
	if args.datetime:
		title_row.append('Date')
	if args.description:
		title_row.append('Description')
	
	# add the header lines
	with open(filename, 'a') as file:
		csv.writer(file, delimiter=',', lineterminator='\n').writerow(title_row)
	print title_row

	# scrape the data
	sites = ["https://thehackernews.com/search?updated-max=2019-01-10T09:39:00%2B01:00&max-results=20&start=20&by-date=false", "https://thehackernews.com/search?updated-max=2018-12-19T09:43:00%2B01:00&max-results=20&start=40&by-date=false", "https://thehackernews.com/search?updated-max=2018-12-03T14:18:00%2B01:00&max-results=20&start=59&by-date=false", "https://thehackernews.com/search?updated-max=2018-11-15T16:09:00%2B01:00&max-results=20&start=78&by-date=false", "https://thehackernews.com/search?updated-max=2018-11-08T10:25:00%2B01:00&max-results=20&start=91&by-date=false", "https://thehackernews.com/search?updated-max=2018-10-19T16:12:00%2B02:00&max-results=20&start=110&by-date=false", "https://thehackernews.com/search?updated-max=2018-10-08T17:34:00%2B02:00&max-results=20&start=130&by-date=false", "https://thehackernews.com/search?updated-max=2018-09-27T21:20:00%2B02:00&max-results=20&start=146&by-date=false", "https://thehackernews.com/search?updated-max=2018-09-19T11:12:00%2B02:00&max-results=20&start=164&by-date=false", "https://thehackernews.com/search?updated-max=2018-09-06T15:08:00%2B02:00&max-results=20&start=184&by-date=false", "https://thehackernews.com/search?updated-max=2018-08-21T10:29:00%2B02:00&max-results=20&start=204&by-date=false", "https://thehackernews.com/search?updated-max=2018-08-08T12:33:00%2B02:00&max-results=20&start=222&by-date=false", "https://thehackernews.com/search?updated-max=2018-07-27T10:31:00%2B02:00&max-results=20&start=242&by-date=false", "https://thehackernews.com/search?updated-max=2018-07-15T09:49:00%2B02:00&max-results=20&start=262&by-date=false", "https://thehackernews.com/search?updated-max=2018-07-05T12:28:00%2B02:00&max-results=20&start=281&by-date=false", "https://thehackernews.com/search?updated-max=2018-06-26T13:53:00%2B02:00&max-results=20&start=299&by-date=false", "https://thehackernews.com/search?updated-max=2018-06-12T20:32:00%2B02:00&max-results=20&start=319&by-date=false", "https://thehackernews.com/search?updated-max=2018-06-05T11:47:00%2B02:00&max-results=20&start=339&by-date=false"]

	for site in sites:
		scrape(site, filename, args.title, args.datetime, args.author, args.description)
	

if __name__ == '__main__':
	main()
