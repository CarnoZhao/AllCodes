from collections import defaultdict

nodes = defaultdict(list)
while True:
	try:
		inp = input().rstrip().split(' -> ')
		key = inp[0]
		nodes[key] = inp[1].split(',')
	except:
		break

cnt = defaultdict(int)
for key in nodes:
	cnt[key] += len(nodes[key])
	for value in nodes[key]:
		cnt[value] -= 1
for key in cnt:
	if cnt[key] == 1:
		start = key
#start = list(nodes.keys())[0]
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
print('->'.join(ret[::-1]))