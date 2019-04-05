s = '{1,6} {1,7} {1,9} {2,3} {2,8} {2,a} {3,9} {3,b} {4,a} {4,c} {5,7} {5,b} {6,8} {6,c} {7,c} {a,b}'
s = s[1:-1].split('} {')
for i, pair in enumerate(s):
	s[i] = pair.split(',')
dic = {}
for pair in s:
	if pair[0] not in dic:
		dic[pair[0]] = [pair[1]]
	else:
		dic[pair[0]].append(pair[1])
	if pair[1] not in dic:
		dic[pair[1]] = [pair[0]]
	else:
		dic[pair[1]].append(pair[0])
dic = dict(sorted(dic.items(), key = lambda x: x[0]))
print(dic)
paths = ['1']
for i in range(12):
	nextpath = []
	for path in paths:
		start = path[-1]
		nextpos = dic[start]
		for nex in nextpos:
			if len(path) == 12 and nex == '1':
				nextpath.append(path + nex)
			elif nex not in path:
				nextpath.append(path + nex)
	paths = nextpath[:]
print(paths)