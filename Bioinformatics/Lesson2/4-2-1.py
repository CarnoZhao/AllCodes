def Score(protein, e_spec, linear):
	prefix = [0]
	for aa in protein:
		prefix.append(prefix[-1] + aa)
	t_spec = [0]
	for i in range(len(prefix)):
		for j in range(i + 1, len(prefix)):
			t_spec.append(prefix[j] - prefix[i])
			if linear == False:
				if i != 0 and j != len(prefix) - 1:#For cycle peptide
					t_spec.append(prefix[-1] - prefix[j] + prefix[i])
	score = 0
	for value in set(t_spec):
		score += min(t_spec.count(value), e_spec.count(value))
	return score

masstable = list(range(57, 201))

e_spec = list(map(lambda x: eval(x), '0 97 99 114 128 147 147 163 186 227 241 242 244 260 261 262 283 291 333 340 357 385 389 390 390 405 430 430 447 485 487 503 504 518 543 544 552 575 577 584 632 650 651 671 672 690 691 738 745 747 770 778 779 804 818 819 820 835 837 875 892 917 932 932 933 934 965 982 989 1030 1039 1060 1061 1062 1078 1080 1081 1095 1136 1159 1175 1175 1194 1194 1208 1209 1223 1225 1322'.split(' ')))
N = 1000

proteins = [[]]
maxscorelist = []
maxscore = 0
mass = 0
especmax = max(e_spec)
while proteins != []:
	print('%.3f%%' % (100 * mass / especmax))
	temp = []
	for protein in proteins:
		for aa in masstable:
			newpro = protein + [aa]
			mass = sum(newpro)
			if mass == especmax:
				lscore = Score(newpro, e_spec, True)
				cscore = Score(newpro, e_spec, False)
				temp.append([newpro, lscore])
				if cscore > maxscore:
					maxscore = cscore
					maxscorelist = [newpro]
				elif cscore == maxscore:
					maxscorelist.append(newpro)
			elif mass < especmax:
				score = Score(newpro, e_spec, True)
				temp.append([newpro, score])
	temp = sorted(temp, key = lambda x: x[1], reverse = True)
	proteins = [x[0] for x in temp[:N]]
	for i in range(N, len(temp)):
		if temp[i][1] == temp[N - 1][1]:
			proteins.append(temp[i][0])
		else:
			break
print(' '.join(['-'.join(map(lambda x: str(x), protein)) for protein in maxscorelist]))



#Wrong answer below
'''while tspecmax <= especmax:
	print('%.3f%%' % (100 * tspecmax / especmax))
	scorelist = []
	for protein in proteins:
		for aa in masstable:
			newpro = protein + [aa]
			score = Score(newpro, e_spec)
			scorelist.append([newpro, score])
	scorelist = sorted(scorelist, key = lambda x: x[1], reverse = True)
	nowmaxscore = scorelist[0][1]
	if nowmaxscore > maxscore:
		maxscore = nowmaxscore
		maxscorelist = []
	for i in range(len(scorelist)):
		if scorelist[i][1] == maxscore:
			maxscorelist.append(scorelist[i][0])
		else:
			break
	proteins = [x[0] for x in scorelist[:N]]
	for i in range(N, len(scorelist)):
		if scorelist[i][1] == scorelist[N - 1][1]:
			proteins.append(scorelist[i][0])
		else:
			break
	tspecmax = min([sum(protein) for protein in proteins])
#maxscorelist = list(set(['-'.join(map(lambda x: str(x), protein)) for protein in maxscorelist]))#SET form
maxscorelist = ['-'.join(map(lambda x: str(x), protein)) for protein in maxscorelist]#LIST form
print(sorted(maxscorelist))
print(maxscore)
print(len(maxscorelist))'''