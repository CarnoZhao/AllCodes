from collections import defaultdict
f = open('relationships_w_pop_121708.txt')
pop_ind = defaultdict(list)
f.readline()
offsprings = []
for l in f:
	toks = l.rstrip().split('\t')
	fam_id, ind_id, mom, dad = (toks[i] for i in range(4))
	if mom != '0' or dad != '0':
		offsprings.append((fam_id, ind_id))
	pop = toks[-1]
	pop_ind[pop].append((fam_id, ind_id))
f.close()