import sys

for line in sys.stdin:
    line = line.strip()
    line = line.split(',')
    origin = line[16]
    dest = line[17]
    taxi_in = line[19]
    taxi_out = line[20]
    if taxi_out.isdigit() or taxi_in.isdigit():
    	print('%s\t%s\t%s\t%s' % (origin, taxi_out, dest, taxi_in))
