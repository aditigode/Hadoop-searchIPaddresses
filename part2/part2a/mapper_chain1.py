import re
import sys

# pat = re.compile('(?P<ip>\d+.\d+.\d+.\d+').*?"\w+ (?P<subdir>.*?) ')
# pat = re.compile("(?P<ip>\d+\d+.\d+.\d+).*?\d{4}:(?P<hour>\d{2}).*? ")
# ?P creates a match group  names ip
range = sys.argv[1]
#print("range is", range)
low, high = range.split("-")

pat = re.compile('(?P<ip>\d+.\d+.\d+.\d+).*?\d{4}:(?P<hour>\d{2}):\d{2}.*? ')



for line in sys.stdin:
    match = pat.search(line)
    if match:
        hour = match.group('hour')
        if int(hour) >= int(low) and int(hour) < int(high):
            print("[" + hour + ":00" + "]" + match.group('ip') + "\t" + "1")


