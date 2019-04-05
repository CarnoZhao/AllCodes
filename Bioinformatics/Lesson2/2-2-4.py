from collections import defaultdict

def make_node(k):
	nodes = defaultdict(list)
	for i in range(2 ** k):
		kmer = bin(i)[2:]
		kmer = '0' * (k - len(kmer)) + kmer
		nodes[kmer[:-1]].append(kmer[1:])
	return nodes

def add_cycle(stack, startnode, nodes):
	while nodes[startnode] != []:
		stack.append(startnode)
		startnode = nodes[startnode].pop()
	stack.append(startnode)
	return stack, nodes

def main():
	k = 9
	nodes = make_node(k)
	startnode = list(nodes.keys())[0]
	stack, queue = [], []
	stack, nodes = add_cycle(stack, startnode, nodes)
	while stack != []:
		if nodes[stack[-1]] == []:
			queue.append(stack.pop())
		else:
			startnode = stack.pop()
			stack, nodes = add_cycle(stack, startnode, nodes)
	queue = queue[::-1][k - 1:]
	queue = queue[0] + ''.join([string[-1] for string in queue[1:]])
	print(queue)
	print(len(queue))

main()