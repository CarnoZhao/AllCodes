from collections import defaultdict

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

f = open('integer_mass_table.txt')
masstable = set([eval(l.rstrip().split(' ')[1]) for l in f])
f.close()

e_spec = list(map(lambda x: eval(x), '0 97 99 113 114 115 128 128 147 147 163 186 227 241 242 244 244 256 260 261 262 283 291 309 330 333 340 347 385 388 389 390 390 405 435 447 485 487 503 504 518 544 552 575 577 584 599 608 631 632 650 651 653 672 690 691 717 738 745 770 779 804 818 819 827 835 837 875 892 892 917 932 932 933 934 965 982 989 1039 1060 1062 1078 1080 1081 1095 1136 1159 1175 1175 1194 1194 1208 1209 1223 1322'.split(' ')))
N = 1000

proteins = [[]]
maxscorelist = []
maxscore = 0
especmax = max(e_spec)
while proteins != []:
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