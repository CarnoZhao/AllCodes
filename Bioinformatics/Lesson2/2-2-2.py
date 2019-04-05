from collections import defaultdict
import os

def file_name(path):
	filelist = os.listdir(path)
	timelist = [os.stat(path + file).st_mtime for file in filelist]
	filename = filelist[timelist.index(max(timelist))]
	return path + filename

def load_file(filename):
	nodes = defaultdict(list)
	f = open(filename)
	for l in f:
		pair = l.rstrip().split(' -> ')
		nodes[pair[0]] = pair[1].split(',')
	f.close()
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

def add_cycle(stack, startnode, nodes):
	while nodes[startnode] != []:
		stack.append(startnode)
		startnode = nodes[startnode].pop()
	stack.append(startnode)
	return stack, nodes

def main():
	path = 'D:/Browser Download/'
	filename = file_name(path)
	nodes = load_file(filename)
	startnode, endnode = count_edge(nodes)
	nodes[endnode].append(startnode)
	stack, queue = [], []
	stack, nodes = add_cycle(stack, startnode, nodes)
	while stack != []:
		if nodes[stack[-1]] == []:
			queue.append(stack.pop())
		else:
			startnode = stack.pop()
			stack, nodes = add_cycle(stack, startnode, nodes)
	queue = queue[1:]
	fw = open('ret.txt', 'w')
	fw.write('->'.join(queue[::-1]))
	fw.close()

main()