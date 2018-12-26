def file_name(path):
	import os
	filelist = os.listdir(path)
	timelist = [os.stat(path + x).st_mtime for x in filelist]
	filename = filelist[timelist.index(max(timelist))]
	return path + filename

def load_file(filename):
	nodes = {}
	f = open(filename)
	for l in f:
		key, value = l.rstrip().split(' -> ')
		value = value.split(',')
		nodes[key] = value
	f.close()
	return nodes

def add_stack(stack, nodes, startnode):
	while startnode in nodes:
		nextnode = nodes[startnode][0]
		stack.append(nextnode)
		if len(nodes[startnode]) == 1:
			del nodes[startnode]
		else:
			del nodes[startnode][0]
		startnode = nextnode
	return stack, nodes

def main():
	path = 'D:/Browser Download/'
	filename = file_name(path)
	nodes = load_file(filename)
	queue = []
	stack = []
	startnode = list(nodes.keys())[0]
	stack.append(startnode)
	while True:
		stack, nodes = add_stack(stack, nodes, startnode)
		try:
			while stack[-1] not in nodes:
				queue.append(stack[-1])
				stack.pop()
		except:
			break
		startnode = stack[-1]
	fw = open('ret.txt', 'w')
	fw.write('->'.join(queue[::-1]))
	fw.close()

main()