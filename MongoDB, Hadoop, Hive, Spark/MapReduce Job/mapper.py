#!/usr/bin/python3
"""mapper.py"""

# input format:  id,YYYY-MM-DD
# output format: YYYY \t MM \t DD \t id

import sys

# create iterator on input lines
lines = sys.stdin

# skip first line (contains column names: listing_id,date)
next(lines)

# iterate over all remaining lines
for line in lines:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split(",")
    # assign elements to single variables
    id_     = words[0]
    #date    = words[1].split("-")
    #year    = date[0]
    #month   = date[1]
    #day     = date[2]
    date = words[1]

    # write the results to STDOUT (standard output);
    # the output here will be the input for the
    # Reduce step, i.e. the input for reducer.py

    #print ( '%s\t%s\t%s\t%s' % (year, month, day, id_) )
    print('%s\t%s' % (date, id_) )
