from collections import defaultdict
import os

path = 'D:/Browser Download/'
filelist = os.listdir(path)
timelist = [os.stat(path + x).st_mtime for x in filelist]
filename = filelist[timelist.index(max(timelist))]
filename = path + filename
pairs = []
f = open(filename)
k, d = tuple(map(lambda x: eval(x), f.readline().rstrip().split(' ')))
for l in f:
	pairs.append(l.rstrip().split('|'))
f.close()
#print(pairs)
'''
pairs = '(AG|AG), (AG|TG), (CA|CT), (CT|CA), (CT|CT), (GC|GC), (GC|GC), (GC|GC), (TG|TG)'
k = 2
d = 1
pairs = list(map(lambda x: [x[1:3], x[4:6]], pairs.split(', ')))
'''
debruijn = defaultdict(list)
for pair in pairs:
	debruijn[pair[0][:-1] + pair[1][:-1]].append(pair[0][1:] + pair[1][1:])

cnt = defaultdict(int)
for pos1 in list(debruijn.keys()):
	cnt[pos1] += 1
	for pos2 in debruijn[pos1]:
		cnt[pos2] -= 1
for pos in cnt:
	if cnt[pos] == 1:
		start = pos
	elif cnt[pos] == -1:
		end = pos
#print(cnt)
del cnt
#fill the cycle

string = []
nextnode = start
stack = [start]
while debruijn != {}:
	if debruijn[nextnode]:
		nextnode = debruijn[nextnode].pop()
		stack.append(nextnode)
	else:
		del debruijn[nextnode]
		string.append(stack.pop())
		try:
			nextnode = stack[-1]
		except:
			break
del stack
string = string[::-1]
#make the string

ret = ''
for i in range(k + d):
	ret += string[i][0]
for i in range(len(string)):
	ret += string[i][k - 1]
print(ret)