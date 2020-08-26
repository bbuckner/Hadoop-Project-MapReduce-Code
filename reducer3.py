import sys
codes = {}
for line in sys.stdin:
    code = line.strip()
    codes[code] = codes.get(code, 0) + 1
print("The most common reason for flight cancellations is: ")
if len(codes) > 0:
	max_code = max(codes, key = codes.get)
	if max_code == 'A':
		print('A - Carrier')
	if max_code == 'B':
		print('B - Weather')
	if max_code == 'C':
		print('C - NAS') # I have no idea what NAS means
	if max_code == 'D':
		print('D - Security')