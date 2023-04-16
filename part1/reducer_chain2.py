from operator import itemgetter
import sys
output_dict = {}

for line in sys.stdin:
    line = line.strip()
    hour, ipaddress ,count = line.split('\t')
    #print(hour, ip, count)

    if hour not in output_dict.keys():
        output_dict[hour] = {}
        output_dict[hour][ipaddress] = int(count)
    else:
        if ipaddress not in output_dict[hour].keys():
            output_dict[hour][ipaddress] = int(count)

#print(output_dict)

for hour, inner_dict in output_dict.items():
    #print(hour)
    inner_dict = sorted(inner_dict.items(), key=itemgetter(1), reverse=True)
    #final_dict[hour] = {}
    top3 = 0
    for ip, count in inner_dict:
        if top3 >= 3:
            break
        #print(hour + "\t" + ip + "\t" + str(count))
        print("["+ hour + "]" + ip + "\t" + str(count))
        #final_dict[hour][ip] = count
        top3 += 1


"""
#sort the dictionary on hour, count
output_dict = sorted(output_dict.items(), key = itemgetter(0))

#output local top3
top3 = 0
previous_hour = ""
for key, ip in output_dict:
    hour, count = key.split(" ")

    if top3 < 3:
        print("[" + hour + "]" + ip + "\t" + count)
        previous_hour = hour
        top3 += 1
    else:
        if previous_hour != hour:

            print("[" + hour + "]" + ip + "\t" + count)
            previous_hour = hour
            top3 = 1
        else:
            pass

"""