from collections import defaultdict
import os

path = 'D:/Browser Download/'
filelist = os.listdir(path)
timelist = [os.stat(path + x).st_mtime for x in filelist]
filename = path + filelist[timelist.index(max(timelist))]
nodes = defaultdict(list)
#filename = '6-1-Sample.txt'
with open(filename) as f:
	for l in f:
		l = l.rstrip().split(' -> ')
		nodes[l[0]] = l[1].split(',')
f.close()

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
fw = open('6-1-Answer.txt', 'w')
for string in ret:
	fw.write(' -> '.join(string) + '\n')
fw.close()
