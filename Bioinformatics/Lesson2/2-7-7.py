from collections import defaultdict

nodes = defaultdict(list)
while True:
	try:
		l = input().rstrip().split(' -> ')
		nodes[l[0]] = l[1].split(',')
	except:
		break

cntin = defaultdict(int)
cntout = defaultdict(int)
for key in nodes:
	cntout[key] += len(nodes[key])
	for value in nodes[key]:
		cntin[value] += 1

ret = []
ls = list(filter(lambda x: cntin[x] != 1 or cntout[x] != 1, nodes.keys()))
for key in ls:#no cycle branches
	while nodes[key]:
		string = [key]
		nextnode = nodes[key].pop()
		while cntout[nextnode] == 1 and cntin[nextnode] == 1:
			string.append(nextnode)
			nextnode = nodes.pop(nextnode).pop()
		string.append(nextnode)
		ret.append(string)
	nodes.pop(key)
del ls
keys = list(nodes.keys())
for key in keys:
	if nodes[key]:
		string = [key]
		while nodes[key]:
			key = nodes.pop(key).pop()
			string.append(key)
		ret.append(string)
		nodes.pop(key)
print('\n'.join(['->'.join(string) for string in ret]))
