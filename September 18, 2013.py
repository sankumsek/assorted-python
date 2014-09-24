#3.37

import math
def collision(x1, y1, r1, x2, y2, r2):
	if (r1+r2) >= math.sqrt(((x2-x1)**2)+((y1-y2)**2)):
		print('True')
	else:
		print('False')

#3.38

def partition(list):
	for name in lst:
		if name[0] < 'N':
			print(name)



