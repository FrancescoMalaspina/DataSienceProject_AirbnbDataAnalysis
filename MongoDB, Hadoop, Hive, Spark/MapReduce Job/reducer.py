#!/usr/bin/python3
"""reducer.py"""

import sys

current_date = None
current_count = 0
date = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input from mapper.py
    date, id_ = line.split('\t', 1)

    # this IF-switch only works because Hadoop sorts map output by key
    if current_date == date:
        current_count += 1
    else:
        if current_date:
            # write current result to STDOUT
            print ('%s\t%s' % (current_date, current_count))
        current_count = 1
        current_date = date

# write the last result to STDOUT
if current_date:
    print ('%s\t%s' % (current_date, current_count))
