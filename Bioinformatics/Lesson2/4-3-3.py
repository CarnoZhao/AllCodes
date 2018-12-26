def loadFile():
	M, N = 20, 1000
	e_spec = sorted(list(map(lambda x: eval(x), '0 97 99 113 114 115 128 128 147 147 163 186 227 241 242 244 244 256 260 261 262 283 291 309 330 333 340 347 385 388 389 390 390 405 435 447 485 487 503 504 518 544 552 575 577 584 599 608 631 632 650 651 653 672 690 691 717 738 745 770 779 804 818 819 827 835 837 875 892 892 917 932 932 933 934 965 982 989 1039 1060 1062 1078 1080 1081 1095 1136 1159 1175 1175 1194 1194 1208 1209 1223 1322'.split(' '))))
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