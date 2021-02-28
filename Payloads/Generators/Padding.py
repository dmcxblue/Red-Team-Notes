#/usr/bin/env python3
#Python3 padding.py [file] [size] [-mb/-kb]

import sys
if len (sys.argv) < 4:
	sys.exit("[Missing Arguments!!\n [+] Usage: Python3 Padding.py [file] [size] [-mb/kb]")

bp = sys.argv[1]
size = int(sys.argv[2])
tp = sys.argv[3]

f = open(bp, 'ab')
if tp == '-kb':
	b_size = size * 1024
elif tp == '-mb':
	b_size = size * 1048576
else:
	sys.exit('[+] Use -mb or -kb!')

buffersize = 256

for i in range(b_size // buffersize):
	f.write(b"0" * buffersize)

f.close()

print ("[+] Finished Padding ", bp, "with ", size, tp)
