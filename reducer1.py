import sys

performance = {}

for line in sys.stdin:
    line = line.strip()
    carrier, on_time = line.split('\t', 1)
    performance[carrier] = performance.get(carrier, [0,0,0])
    performance[carrier][int(on_time)] += 1
    performance[carrier][2] = performance[carrier][0] / (performance[carrier][0] + performance[carrier][1])
    
sorted_list = sorted(performance.items(), key = lambda kv: kv[1][2])

# Low on-time percentage is bad
# High on-time percentage is good
print('Bottom 3 Carriers by On-Time Percentage')
for i in range(3):
	print('%s\t%s%%' % (sorted_list[i][0], round(sorted_list[i][1][2] * 100, 3)))

print('Top 3 Carriers by On-Time Percentage')
for i in range(1, 4):
    	print('%s\t%s%%' % (sorted_list[-i][0], round(sorted_list[-i][1][2] * 100, 3)))