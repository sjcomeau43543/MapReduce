#!/usr/bin/env python
import sys

def main():
	for line in sys.stdin:
	    # remove leading and trailing whitespace
	    line = line.strip()

	    words = line.split()

	    for word in words:
		# write output to the stdout so the reducer can get it
		# tab delimited
			print '%s\t%s' % (word, 1)

if __name__ == "__main__":
	main()
