from collections import defaultdict
import copy
pairs = []
k, d = tuple(map(lambda x: eval(x), input().rstrip().split(' ')))
while True:
	try:
		pairs.append(input().rstrip().split('|'))
	except:
		break

ret = ''
match = 1
for i in range(d + 2, len(pairs)):
	if pairs[i][0][-1] != pairs[i - d - 2][1][0]:
		match = 0
		break
if match == 1:
	ret += pairs[0][0][:-1]
	for i in range(d + 2):
		ret += pairs[i][0][-1]
	ret += pairs[0][1][:-1]
	for i in range(d + 2, len(pairs)):
		ret += pairs[i][1][-1]
print(ret)