try:
	import pygraphviz as pgv
except:
	pass
from collections import defaultdict
from copy import deepcopy

class OneSquare(object):
	"""One square with four nodes of peptide and two pairs of same amino acid
		A  -a-> aA
		:        :
		b        b
		:        :
		Ab -a-> aAb"""
	def __init__(self, pairs):
		super(OneSquare, self).__init__()
		self.n0 = pairs[0]
		self.a1 = pairs[1]
		self.a2 = pairs[2]
		self.n1 = pairs[3]
		self.n2 = pairs[4]
		self.n3 = pairs[5]
		self.right = []
		self.left = []
		self.up = []
		self.down = []	
		self.diag = []

	def detail(self, PRINT = True, COMPACT = False):
		if COMPACT:
			string = '%s, %s\n%s, %s\n%s, %s' % (self.n0, self.n1, self.n2, self.n3, self.a1, self.a2)
		else:
			string = '%s\t-%s->\t%s\n  |  \t\t\t  |\n %s \t\t\t %s\n  |  \t\t\t  |\n%s\t-%s->\t%s' %\
				(self.n0, self.a1, self.n1, self.a2, self.a2, self.n2, self.a1, self.n3)
		if PRINT:
			print(string + '\n')
		return string

	def trans(self):
		pairs = [self.n0, self.a2, self.a1, self.n2, self.n1, self.n3]
		return OneSquare(pairs)

def Function0(err = 0.3, tablefull = False):
	e_spec = list(map(lambda x: eval(x), '371.5 375.4 390.4 392.2 409.0 420.2 427.2 443.3 446.4 461.3 471.4 477.4 491.3 505.3 506.4 519.2 536.1 546.5 553.3 562.3 588.2 600.3 616.2 617.4 618.3 633.4 634.4 636.2 651.5 652.4 702.5 703.4 712.5 718.3 721.0 730.3 749.4 762.6 763.4 764.4 779.6 780.4 781.4 782.4 797.3 862.4 876.4 877.4 878.6 879.4 893.4 894.4 895.4 896.5 927.4 944.4 975.5 976.5 977.4 979.4 1005.5 1007.5 1022.5 1023.7 1024.5 1039.5 1040.3 1042.5 1043.4 1057.5 1119.6 1120.6 1137.6 1138.6 1139.5 1156.5 1157.6 1168.6 1171.6 1185.4 1220.6 1222.5 1223.6 1239.6 1240.6 1250.5 1256.5 1266.5 1267.5 1268.6'.split(' ')))
	if tablefull == True:
		masstable = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 132, 137, 147, 156, 163, 186]
	else:
		masstable = [99, 128, 113, 147, 97, 186, 114, 163]
	lenth = len(e_spec)
	aanum = len(masstable)
	fw = open('ProteinNode.txt', 'w')
	for idx1 in range(lenth):
		target = e_spec[idx1]
		cnt = 0
		for i in range(aanum):
			target2 = target + masstable[i]
			for idx2 in range(idx1 + 1, lenth):
				specnum = e_spec[idx2]
				if target2 > specnum - err and target2 < specnum + err:
					fw.write('%.1f\t%d\t%.1f\n' % (target, masstable[i], specnum))
					cnt += 1
	fw.close()
	print("\n\n\n\nProteinNode.txt has been changed, with %.1f err and %s table." % \
		(err, 'FULL' if tablefull == True else 'PARTIAL'))
	print('You can set err using the first parameter,')
	print('and choose full table (True) or partial table (False) using the second parameter.\n\n\n')

def Function1():
	nodesset = set()
	nodes = defaultdict(list)
	f = open('ProteinNode.txt')
	for l in f:
		l = l.rstrip().split('\t')
		nodes[l[0]].append(l[-1])
		nodesset.add(l[0])
		nodesset.add(l[-1])
	f.close()
	try:
		g = pgv.AGraph()
		for key in nodesset:
			g.add_node(key)
		for key in nodes:
			for value in nodes[key]:
				g.add_edge(key, value)
		g.layout()
		g.draw('NodesTree.png')
	except:
		print('\n\n\n\n\nPlease run in Linux-Bioinformatics\n\n\n\n\n')

def Function2(WRITE = True):
	nodes = defaultdict(dict)
	f = open('ProteinNode.txt')
	for l in f:
		l = l.rstrip().split('\t')
		nodes[l[0]][l[1]] = l[-1]
	storelist = []
	exist = set()
	nodes = dict(nodes)
	for pep in nodes:
		for key1 in nodes[pep]:
			pep1 = nodes[pep][key1]
			if pep1 not in nodes:
				continue
			for key2 in nodes[pep1]:
				if key2 == key1:
					continue
				pep3 = nodes[pep1][key2]
				if key2 not in nodes[pep]:
					continue
				pep2 = nodes[pep][key2]
				if pep2 not in nodes:
					continue
				if key1 not in nodes[pep2]:
					continue
				pep4 = nodes[pep2][key1]
				if pep3 == pep4:
					ls = [pep, key1, key2, pep1, pep2, pep3]
					string = ','.join(sorted(ls))
					if string not in exist:
						exist.add(string)
						storelist.append(ls)
	if WRITE:
		fw = open('ProteinNode2.txt', 'w')
		for x in storelist:
			fw.write(','.join(x) + '\n')
		fw.close()
	return storelist

def Function3():
	storelist = Function2(False)
	setnet = set()
	nets = []
	for peps1 in storelist:
		for peps2 in storelist:
			if peps1[0] == peps2[0]:
				continue
			if peps1[3] in peps2 and peps1[4] not in peps2:
				samenode = peps1[3]
			elif peps1[3] not in peps2 and peps1[4] in peps2:
				samenode = peps1[4]
			else:
				continue
			for peps in storelist:
				if peps[0] != samenode:
					continue
				if (peps[3] == peps1[-1] and peps[4] == peps2[-1]) or \
					(peps[4] == peps1[-1] and peps[3] == peps2[-1]):
					ls = [peps1[0], peps2[0], peps1[3], peps1[4], peps2[3], peps2[4], samenode, peps1[-1], peps2[-1], peps[-1]]
					if tuple(sorted(ls)) not in setnet:
						setnet.add(tuple(sorted(ls)))
						nets.append(ls)
	for net in sorted(nets):
		part = net[2:6]
		for i in range(len(part)):
			if i in (0, 1) and part[i] != net[6]:
				node1 = part[i]
			elif i in (2, 3) and part[i] != net[6]:
				node2 = part[i]
		print('       %s--%s' % (net[0], node1))
		print('         |      |')
		print('%s--%s--%s' % (net[1], net[6], net[7]))
		print('  |      |      |')
		print('%s--%s--%s' % (node2, net[8], net[9]))
		'''
		print('       \t%s\t%s' % (net[0], node1))
		print('%s\t%s\t%s' % (net[1], net[6], net[7]))
		print('%s\t%s\t%s' % (node2, net[8], net[9]))
		'''
		print('\n')

def Function4():
	storelist = Function2(False)
	squares = []
	for pairs in storelist:
		squares.append(OneSquare(pairs))
	for i in range(len(squares)):
		sq1 = squares[i]
		for j in range(i + 1, len(squares)):
			sq2 = squares[j]
			if sq2.n0 == sq1.n1:
				if sq1.n3 not in (sq2.n1, sq2.n2):
					continue
				#elif sq1.n3 == sq2.n1:
				#	squares[j] = sq2 = sq2.trans()
				sq1.right.append(sq2)
				sq2.left.append(sq1)
			elif sq2.n0 == sq1.n2:
				if sq1.n3 not in (sq2.n1, sq2.n2):
					continue
				#elif sq1.n3 == sq2.n2:
				#	squares[j]  = sq2 = sq2.trans()
				sq1.down.append(sq2)
				sq2.up.append(sq1)
	squares = list(filter(lambda x: x.right + x.left + x.up + x.down != [], squares))
	return squares
	
def Function5():
	squares = Function4()
	try:
		g = pgv.AGraph()
		for square in squares:
			g.add_node(square.detail(False, True))
		for square in squares:
			for value in square.right + square.down:
				if value.n0 == square.n1:
					if value.n2 == square.n3:
						g.add_edge(square.detail(False, True), value.detail(False, True), color = 'red')
					else:
						g.add_edge(square.detail(False, True), value.detail(False, True), color = 'orange')
				else:
					if value.n1 == square.n3:
						g.add_edge(square.detail(False, True), value.detail(False, True), color = 'blue')
					else:
						g.add_edge(square.detail(False, True), value.detail(False, True), color = 'green')
			''':
				g.add_edge(square.detail(False, True), value.detail(False, True), color = 'red')
			for value in square.down:
				g.add_edge(square.detail(False, True), value.detail(False, True), color = 'blue')
				'''
		g.layout('dot')
		g.draw('SquareNet.png')
	except:
		print('\n\n\n\n\nPlease run in Linux-Bioinformatics\n\n\n\n\n')

#Function0(default err = 0.3, fulltable = False) = changeProteinNode
#Function1 = printNodeTree1
#Function2(default WRITE = Ture) = changeProteinNode2
#Function3 = makeNet
#Function4 = squareMakeNet
#Function5 = printSquareNet
Function0()
Function5()