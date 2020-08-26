import sys

for line in sys.stdin:
    line = line.strip().split(',')
    carrier = line[8]
    arrDelay = line[14]
    try:
        if float(arrDelay) > 0:
            print('%s\t%s' % (carrier, 1))
        else:
            print('%s\t%s' % (carrier, 0))    
    except ValueError:
        continue
