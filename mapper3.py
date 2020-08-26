import sys

codes = ['A', 'B', 'C', 'D']

for line in sys.stdin:
    line = line.strip().split(',')
    code = line[22]
    if code.upper() in codes:
    	print(code)
