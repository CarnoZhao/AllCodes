from LoadFile import LoadFile
from collections import defaultdict

def loadFile():
	f = open(LoadFile())
	M = eval(f.readline().rstrip())
	N = eval(f.readline().rstrip())
	e_spec = sorted(list(map(lambda x: eval(x), f.readline().rstrip().split(' '))))
	f.close()
	#Example
	'''
	M, N = 20, 60
	e_spec = sorted(list(map(lambda x: eval(x), '0 57 57 71 99 129 137 170 186 194 208 228 265 285 299 307 323 356 364 394 422 493'.split(' '))))
	'''
	'''
	M, N = 20, 273
	e_spec = sorted(list(map(lambda x: eval(x), '853 113 585 796 924 502 423 1210 342 186 761 391 593 1412 1152 1396 260 129 1381 229 242 356 990 1047 57 748 1176 730 990 1038 1119 294 339 114 696 1251 1267 617 567 357 471 163 1266 1281 0 536 1395 454 1104 1362 1039 892 1509 1086 129 649 1095 713 258 777 1394 753 299 599 648 876 414 1249 813 242 859 1305 552 1284 861 650 1249 261 520 470 519 957 1233 405 260 861 762 810 1248 891 916 1346 390 981 147 1323 390 732 618 1380 1038 756 989 225 633 910 204 1452 243 1119 860 1395 129 57 503 1267 1153 276 462 228 1215 114 1170 357 973 388 519 699 131 128 1120 648 1452 1055 632 333 1380 528 747 389 656 97 1167 779 1380 1280 942 115 1121 1152 1007 990 1006 1118 519 877 1378 471'.split(' '))))
	'''
	return M, N, e_spec

def Score(protein, e_spec, linear):
	prefix = [0]
	for aa in protein:
		prefix.append(prefix[-1] + aa)
	lenth = len(prefix)
	t_spec = [0]
	for i in range(lenth):
		for j in range(i + 1, lenth):
			t_spec.append(prefix[j] - prefix[i])
			if linear != 'linear':
				if i != 0 and j != lenth - 1:
					t_spec.append(prefix[-1] - prefix[j] + prefix[i])
	score = 0
	for value in set(t_spec):
		score += min(t_spec.count(value), e_spec.count(value))
	return score

def convolutionFunc(e_spec, M):
	conv = []
	lenth = len(e_spec)
	for i in range(lenth):
		for j in range(i + 1, lenth):
			conv.append(e_spec[j] - e_spec[i])
	conv = list(filter(lambda x: x >= 57 and x <= 200, conv))
	conv = sorted([[num, conv.count(num)] for num in set(conv)], key = lambda x: x[1], reverse = True)
	mostcnt = [ls[0] for ls in conv][:M]
	for i in range(M, len(conv)):
		if conv[i][1] == conv[M - 1][1]:
			mostcnt.append(conv[i][0])
		else:
			break
	return mostcnt

def Sequence(e_spec, N, acidlist):
	proteins = [[]]
	parentmass = max(e_spec)
	maxscore = 0
	maxlist = []
	while proteins != []:
		temp = []
		for protein in proteins:
			for aa in acidlist:
				newpro = protein + [aa]
				newmass = sum(newpro)
				if newmass == parentmass:
					linescore = Score(newpro, e_spec, 'linear')
					cyclscore = Score(newpro, e_spec, 'cycle')
					temp.append([newpro, linescore])
					if cyclscore > maxscore:
						maxscore = cyclscore
						maxlist = [newpro]
					elif cyclscore == maxscore:
						maxlist.append(newpro)
				elif newmass < parentmass:
					linescore = Score(newpro, e_spec, 'linear')
					temp.append([newpro, linescore])
		temp = sorted(temp, key = lambda x: x[1], reverse = True)
		proteins = [x[0] for x in temp[:N]]
		for i in range(N, len(temp)):
			if temp[i][1] == temp[N - 1][1]:
				proteins.append(temp[i][0])
			else:
				break
	return maxlist

def main():
	M, N, e_spec = loadFile()
	acidlist = convolutionFunc(e_spec, M)
	maxlist = Sequence(e_spec, N, acidlist)
	print('\n'.join(set(['-'.join(map(lambda x: str(x), protein)) for protein in maxlist])))
	#Sample out = 99-71-137-57-72-57

main()