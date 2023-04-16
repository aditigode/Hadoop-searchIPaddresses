import re
import sys

#pat = re.compile('(?P<ip>\d+.\d+.\d+.\d+').*?"\w+ (?P<subdir>.*?) ')
pat = re.compile("(?P<ip>\d+\d+.\d+.\d+).+?\w+ (?P<subdir>.*?) ")
#P creates a match group  names ip


for line in sys.stdin:
    match = pat.search(line)
    if match:
        print(match.group('ip')+"\t"+"1")

