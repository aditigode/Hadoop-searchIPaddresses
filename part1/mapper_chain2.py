import re
import sys
from operator import itemgetter

nested_dict = {}

for line in sys.stdin:
    line = line.strip()
    ip, count = line.split('\t')
    # print(ip, count)
    index = ip.find(']')
    hour, ipaddress = ip[1:index], ip[index + 1:]
    # print("hour",hour)
    # print("ipaddess",ipaddress)

    if hour not in nested_dict.keys():
        nested_dict[hour] = {}
        nested_dict[hour][ipaddress] = int(count)
    else:
        if ipaddress not in nested_dict[hour].keys():
            nested_dict[hour][ipaddress] = int(count)
    # print(nested_dict)

# nested_dict = sorted(nested_dict.items(), key= lambda x : x[1], reverse=True)
# inal_dict = {}
for hour, inner_dict in nested_dict.items():
    # print(hour)
    inner_dict = sorted(inner_dict.items(), key=itemgetter(1), reverse=True)
    # final_dict[hour] = {}
    top3 = 0
    for ip, count in inner_dict:
        if top3 >= 3:
            break
        print(hour + "\t" + ip + "\t" + str(count))
        # final_dict[hour][ip] = count
        top3 += 1