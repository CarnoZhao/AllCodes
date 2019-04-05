import os
from collections import defaultdict

def file_name(path):
	filelist = os.listdir(path)
	timelist = [os.stat(path + file).st_mtime for file in filelist]
	filename = filelist[timelist.index(max(timelist))]
	return path + filename

def load_file(filename):
	f = open(filename)
	k = eval(f.readline().rstrip())
	kmers = [l.rstrip() for l in f]
	return k, kmers

def make_nodes(kmers):
	nodes = defaultdict(list)
	for kmer in kmers:
		nodes[kmer[:-1]].append(kmer[1:])
	return nodes

def count_edge(nodes):
	count = defaultdict(int)
	for key, values in nodes.items():
		count[key] += len(values)
		for value in values:
			count[value] -= 1
	for node, cnt in count.items():
		if cnt == 1:
			startnode = node
		elif cnt == -1:
			endnode = node
	return startnode, endnode

def add_stack(nodes, startnode, stack):
	while nodes[startnode] != []:
		stack.append(startnode)
		startnode = nodes[startnode].pop()
	stack.append(startnode)
	return stack, nodes

def queue_dna(queue):
	queue = queue[1:][::-1]
	dna = queue[0]
	for i in range(1, len(queue)):
		dna += queue[i][-1]
	return dna

def main():
	path = 'D:/Browser Download/'
	filename = file_name(path)
	k, kmers = load_file(filename)
	nodes = make_nodes(kmers)
	startnode, endnode = count_edge(nodes)
	nodes[endnode].append(startnode)
	stack, queue = [], []
	stack, nodes = add_stack(nodes, startnode, stack)
	while stack != []:
		if nodes[stack[-1]] == []:
			queue.append(stack.pop())
		else:
			startnode = stack.pop()
			stack, nodes = add_stack(nodes, startnode, stack)
	dna = queue_dna(queue)
	print(dna)

main()