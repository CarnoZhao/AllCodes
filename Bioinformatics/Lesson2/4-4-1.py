def loadFile():
	M, N = 20, 4000
	e_spec = list(map(lambda x: eval(x), '371.5 375.4 390.4 392.2 409.0 420.2 427.2 443.3 446.4 461.3 471.4 477.4 491.3 505.3 506.4 519.2 536.1 546.5 553.3 562.3 588.2 600.3 616.2 617.4 618.3 633.4 634.4 636.2 651.5 652.4 702.5 703.4 712.5 718.3 721.0 730.3 749.4 762.6 763.4 764.4 779.6 780.4 781.4 782.4 797.3 862.4 876.4 877.4 878.6 879.4 893.4 894.4 895.4 896.5 927.4 944.4 975.5 976.5 977.4 979.4 1005.5 1007.5 1022.5 1023.7 1024.5 1039.5 1040.3 1042.5 1043.4 1057.5 1119.6 1120.6 1137.6 1138.6 1139.5 1156.5 1157.6 1168.6 1171.6 1185.4 1220.6 1222.5 1223.6 1239.6 1240.6 1250.5 1256.5 1266.5 1267.5 1268.6'.split(' ')))
	#e_spec = [371, 375, 391, 392, 409, 420, 427, 443, 447, 461, 471, 478, 492, 506, 507, 519, 536, 547, 554, 562, 588, 600, 616, 617, 618, 634, 634, 637, 652, 652, 703, 704, 712, 718, 721, 730, 749, 762, 763, 765, 780, 780, 781, 782, 797, 863, 876, 877, 879, 880, 894, 894, 896, 897, 927, 944, 976, 976, 978, 980, 1005, 1008, 1022, 1024, 1025, 1039, 1041, 1043, 1044, 1058, 1119, 1120, 1138, 1138, 1139, 1156, 1157, 1168, 1172, 1185, 1221, 1222, 1224, 1240, 1240, 1251, 1256, 1266, 1267, 1268]
	real_spec = [0, 97, 99, 113, 114, 128, 128, 147, 147, 163, 186, 227, 241, 242, 244, 260, 261, 262, 283, 291, 333, 340, 357, 388, 389, 390, 390, 405, 430, 430, 447, 485, 487, 503, 504, 518, 543, 544, 552, 575, 577, 584, 631, 632, 650, 651, 671, 672, 690, 691, 738, 745, 747, 770, 778, 779, 804, 818, 819, 835, 837, 875, 892, 892, 917, 932, 932, 933, 934, 965, 982, 989, 1031, 1039, 1060, 1061, 1062, 1078, 1080, 1081, 1095, 1136, 1159, 1175, 1175, 1194, 1194, 1208, 1209, 1223, 1225, 1322]
	from LoadFile import LoadFile
	masstable = []
	f = open('integer_mass_table.txt')
	for l in f:
		masstable.append(eval(l.rstrip().split(' ')[1]))
	f.close()
	return M, N, e_spec, masstable, real_spec

def Score(protein, e_spec, err, linear, scoreprint):
	prefix = [0]
	for aa in protein:
		prefix.append(prefix[-1] + aa)
	lenth = len(prefix)
	t_spec = [[0, '00']]
	for i in range(lenth):
		for j in range(i + 1, lenth):
			t_spec.append([prefix[j] - prefix[i], '[%d->%d)' % (i, j)])
			if linear != 'linear':
				if i != 0 and j != lenth - 1:
					t_spec.append([prefix[-1] - prefix[j] + prefix[i], '[%d->%d)' % (j, i)])
	t_spec = sorted(t_spec, key = lambda x: x[0])
	score = 0
	#for value in set(t_spec):
	#	score += min(t_spec.count(value), e_spec.count(value))
	i, j = 0, 0
	while i < len(e_spec) and j < len(t_spec):
		e, t = e_spec[i], t_spec[j][0] + 1
		if t >= e - err and t <= e + err:
			if scoreprint == True:
				print("e%.1f ~= t%.1f, %s" % (e, t, t_spec[j][1]))
			score += 1
			i, j = i + 1, j + 1
		elif t < e - err:
			j += 1
		else:
			i += 1
	return score

def diffChange(diff, masstable):
	mind = 200 - 57
	ret = 0
	for aa in masstable:
		div = abs(diff - aa)
		if div < mind:
			mind = div
			ret = aa
	return ret

def convolutionFunc(e_spec, M, masstable):
	conv = []
	lenth = len(e_spec)
	for i in range(lenth):
		for j in range(i + 1, lenth):
			diff = e_spec[j] - e_spec[i]
			conv.append(diff)
	conv = list(filter(lambda x: x >= 54 and x <= 189, conv))
	conv = sorted([[num, conv.count(num)] for num in set(conv)], key = lambda x: x[1], reverse = True)
	'''print(dict(conv))
	newconv = dict([[diffChange(x[0], masstable), x] for x in conv])
	print(newconv)'''
	mostcnt = [ls[0] for ls in conv][:M]
	for i in range(M, len(conv)):
		if conv[i][1] == conv[M - 1][1]:
			mostcnt.append(conv[i][0])
		else:
			break
	mostcnt = list(set([diffChange(x, masstable) for x in mostcnt]))
	return mostcnt

def Sequence(e_spec, N, acidlist, real_spec):
	proteins = [[]]
	maxscore = 0
	maxlist = []
	for i in range(10):
		print(i, end = '')
		temp = []
		for protein in proteins:
			for aa in acidlist:
				newpro = protein + [aa]
				linescore = Score(newpro, e_spec, 0.7, 'linear', False)
				cyclscore = Score(newpro, e_spec, 0.7, 'cycle', False)
				temp.append([newpro, linescore])
				if cyclscore > maxscore:
					maxscore = cyclscore
					maxlist = [newpro]
				elif cyclscore == maxscore and newpro not in maxlist:
					maxlist.append(newpro)
		temp = sorted(temp, key = lambda x: x[1], reverse = True)
		proteins = [x[0] for x in temp[:N]]
		for i in range(N, len(temp)):
			if temp[i][1] == temp[N - 1][1]:
				proteins.append(temp[i][0])
			else:
				break
	print('')
	return maxlist

def main():
	M, N, e_spec, masstable, real_spec = loadFile()
	acidlist = convolutionFunc(e_spec, M, masstable)
	print(acidlist)
	#acidlist = list(set(map(lambda x: eval(x), '99-128-113-147-97-186-147-114-128-163'.split('-'))))
	maxlist = Sequence(e_spec, N, acidlist, real_spec)
	#print('\n'.join(set([' '.join(map(lambda x: str(x), protein)) for protein in maxlist])))
	#print('\n'.join(set(['-'.join(map(lambda x: str(x), protein)) for protein in maxlist])))
	#pep = [97, 163, 97, 147, 147, 114, 128, 113, 114, 163]
	for pep in maxlist:
		print(Score(pep, e_spec, 0.7, 'cycle', False))
		'''
		for x in pep:
			print(x, end = '\t')
		print()
		for i in range(10):
			print(i, end = '\t')
		print()
		'''
		print(' '.join([str(x) for x in pep]))
	#Correct out = 99 128 113 147 97 186 147 114 128 163
	#               0   1   2   3  4   5   6   7   8   9

main()