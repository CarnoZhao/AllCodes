from collections import defaultdict
k = 4
nodes = defaultdict(list)
for i in range(2 ** k):
	bi = '0' * (k - len(bin(i)) + 2) + bin(i)[2:]
	nodes[bi[1:]].append(bi[:-1])

start = list(nodes.keys())[0]
stack = [start]
ret = []
while stack != []:
	try:
		start = nodes[start].pop()
		stack.append(start)
	except:
		nodes.pop(start)
		ret.append(stack.pop())
		if len(stack) >= 1:
			start = stack[-1]
print(''.join([ret[i][-1] for i in range(len(ret) - 1)]))