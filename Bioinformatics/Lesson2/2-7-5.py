from collections import defaultdict
kmers = []
while True:
	try:
		kmers.append(input().rstrip())
	except:
		break
nodes = defaultdict(list)
for kmer in kmers:
	nodes[kmer[:-1]].append(kmer[1:])
#make nodes dictionary

cntin = defaultdict(int)
cntout = defaultdict(int)
for key in nodes:
	cntout[key] += len(nodes[key])
	for value in nodes[key]:
		cntin[value] += 1
#count the in and out route

ret = []
for key in nodes:
	if cntin[key] != 1 or cntout[key] != 1:
		for nextnode in nodes[key]:
			string = key
			while cntin[nextnode] == 1 and cntout[nextnode] == 1:
				string += nextnode[-1]
				nextnode = nodes[nextnode][0]
			string += nextnode[-1]
			ret.append(string)
print(' '.join(ret))