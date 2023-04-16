from operator import itemgetter
import sys
import re


range_dict = {}

for line in sys.stdin:
    line = line.strip()
    ip, count = line.split('\t')

    if ip not in range_dict.keys():
        range_dict[ip] = int(count)
    else:
        range_dict[ip] += int(count)

#rint(range_dict)
range_dict = sorted(range_dict.items(), key = itemgetter(1), reverse=True)

top3 = 0
for ip, count in range_dict:
    if top3 < 3:
        print(ip + "\t" + str(count))
        top3 += 1