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

def cycles_make(nodes):
	cycles = []
	while nodes != {}:
		startnode = list(nodes.keys())[0]
		cycle = [startnode]
		while True:
			nextnode = nodes[startnode][0]
			if nextnode not in cycle:
				cycle.append(nextnode)
			else:
				cycle = cycle[cycle.index(nextnode):] + [nextnode]
				cycles.append(cycle)
				break
			startnode = nextnode
		for i in range(len(cycle) - 1):
			if len(nodes[cycle[i]]) > 1:
				del nodes[cycle[i]][0]
			else:
				del nodes[cycle[i]]
	return cycles

def result_make(cycles):
	result = cycles[0]
	del cycles[0]
	while cycles != []:
		j = 0
		while j < len(result):
			node = result[j]
			i = 0
			while i < len(cycles):
				try:
					cycle = cycles[i]
				except:
					break
				if node in cycle:
					idx1 = result.index(node)
					idx2 = cycle.index(node)
					result = result[:idx1] + cycle[idx2:-1] + cycle[:idx2] + result[idx1:]
					del cycles[i]
				i += 1
			j += 1
	return result

def main():
	path = 'D:/Browser Download/'
	filename = file_name(path)
	nodes = load_file(filename)
	cycles = cycles_make(nodes)
	result = result_make(cycles)
	fw = open('ret.txt', 'w')
	fw.write('->'.join(result))
	fw.close()

main()