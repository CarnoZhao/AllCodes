shape = '\n'.join(["+------------+",
                   "|            |",
                   "|            |",
                   "|            |",
                   "+------+-----+",
                   "|      |     |",
                   "|      |     |",
                   "+------+-----+"])
shape = '\n'.join(["+------------+",
                   "|            |",
                   "|  +---------+",
                   "|  |         |",
                   "|  +---+-----+",
                   "|      |",
                   "+--+---+",
                   "|  |   |",
                   "+--+---+"])

def loadShape(shape):
	shape = shape.split('\n')
	r, c = len(shape), max([len(x) for x in shape])
	shape = [list(x) + [' '] * max(c - len(x), 0) for x in shape]
	return shape, r, c

def makeNodes(shape, r, c):
	nodes = {}
	for i in range(r):
		prenode, paired = None, True
		for j in range(c):
			if shape[i][j] == '+':
				if (i, j) not in nodes:
					nodes[(i, j)] = [None, None, None, None]#[right, down, left, up]
				if prenode != None and not paired:
					nodes[prenode][0], nodes[(i, j)][2] = (i, j), prenode
					paired = True
				prenode = (i, j)
			elif shape[i][j] == '-':
				paired = False
	for j in range(c):
		prenode, paired = None, True
		for i in range(r):
			if (i, j) in nodes:
				if prenode != None and not paired:
					nodes[prenode][1], nodes[(i, j)][3] = (i, j), prenode
					paired = True
				prenode = (i, j)
			elif shape[i][j] == '|':
				paired = False
	return nodes

def link(nodes):
	allrouts, sortedrouts = [], []
	for startnode in nodes:
		rout, node, turn = [startnode], startnode, 0
		if nodes[startnode][turn] == None:
			continue
		while True:
			if startnode in nodes[node] and len(rout) != 2:
				find = sorted(set(rout)) == sorted(rout)
				break
			while nodes[node][turn] == None:
				turn = (turn - 1) % 4
			node = nodes[node][turn]
			rout.append(node)
			turn = (turn + 1) % 4
		if rout[0][0] == min([x[0] for x in rout]) and sorted(rout) not in sortedrouts and find:
			allrouts.append(rout)
			sortedrouts.append(sorted(rout))
		print(rout)
	return allrouts

def makeSolution(allrouts):
	rets = []
	for rout in allrouts:
		mr, mc = min([x[0] for x in rout]), min([x[1] for x in rout])
		rout = [(x[0] - mr, x[1] - mc) for x in rout]
		ret = []
		r, c = max([x[0] for x in rout]) + 1, max([x[1] for x in rout]) + 1
		for i in range(r):
			ret.append([])
			for j in range(c):
				ret[i].append(' ')
		for n in range(-1, len(rout) - 1):
			hori = bool(rout[n][0] == rout[n + 1][0])
			if hori:
				ret[rout[n][0]][rout[n][1]] = ret[rout[n + 1][0]][rout[n + 1][1]] = '+'
				for j in range(min(rout[n][1], rout[n + 1][1]) + 1, max(rout[n][1], rout[n + 1][1])):
					ret[rout[n][0]][j] = '-'
			else:
				ret[rout[n][0]][rout[n][1]] = ret[rout[n + 1][0]][rout[n + 1][1]] = '+'
				for i in range(min(rout[n][0], rout[n + 1][0]) + 1, max(rout[n][0], rout[n + 1][0])):
					ret[i][rout[n][1]] = '|'
		for i in range(r):
			for j in range(c):
				try:
					ret[i][j] = '-' if ret[i][j] == '+' and ret[i][j - 1] == ret[i][j + 1] == '-' else ret[i][j]
				except:
					pass
				try:
					ret[i][j] = '|' if ret[i][j] == '+' and ret[i - 1][j] == ret[i + 1][j] == '|' else ret[i][j]
				except:
					pass
		rets.append('\n'.join([''.join(x).rstrip() for x in ret]))
	return rets


def break_pieces(shape):
	print(shape)
	shape, r, c = loadShape(shape)
	nodes = makeNodes(shape, r, c)
	allrouts = link(nodes)
	solutions = makeSolution(allrouts)
	return sorted(solutions)

print('\n\n'.join(break_pieces(shape)))
