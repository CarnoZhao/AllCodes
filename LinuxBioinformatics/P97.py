from collections import defaultdict

f = open('relationships_w_pop_121708.txt')
pop_ind = defaultdict(list)
f.readline() # header
for line in f:
	toks = line.rstrip().split('\t')
	fam_id = toks[0]
	ind_id = toks[1]
	pop = toks[-1]
	pop_ind[pop].append((fam_id, ind_id))
f.close()

'''all_inds = []
for inds in pop_ind.values():
	all_inds.extend(inds)
for line in open('hapmap1.ped'):
	toks = line.rstrip().replace(' ', '\t').split('\t')
	fam = toks[0]
	ind = toks[1]
	if (fam, ind) not in all_inds:
		print('Problem with %s/%s' % (fam, ind))'''

from genomics.popgen.plink.convert import to_genepop
to_genepop('hapmap1_auto', 'hapmap1_auto', pop_ind)
to_genepop('hapmap10', 'hapmap10', pop_ind)
to_genepop('hapmap10_auto', 'hapmap10_auto', pop_ind)
to_genepop('hapmap10_auto_noofs_ld', 'hapmap10_auto_noofs_ld', pop_ind)
to_genepop('hapmap10_auto_noofs_2', 'hapmap10_auto_noofs_2', pop_ind) # Have finished

'''from Bio.PopGen.GenePop import read
rec = read(open('hapmap1_auto.gp'))
print('Number of loci %d' % len(rec.loci_list))
print('Number of populations %d' % len(rec.pop_list))
print('Population names: %s' % ','.join(rec.pop_list))
print('Individuals per population %s' % ','.join([str(len(inds)) for inds in rec.populations]))
ind = rec.populations[1][0]
print('Individual %s, SNP %s, alleles: %d %d' % (ind[0], rec.loci_list[0], ind[1][0][0], ind[1][0][1]))
del rec

from Bio.PopGen.GenePop.LargeFileParser import read as read_large
def count_individuals(fname):
	rec = read_large(open(fname))
	pop_size = []
	for line in rec.data_generator():
		if line == ():
			pop_size.append(0)
		else:
			pop_size[-1] += 1
	return pop_size

print('Individuals per population %s' % ','.join([str(inds) for inds in count_individuals('hapmap1_auto.gp')]))
print(len(read_large(open('hapmap10.gp')).loci_list))
print(len(read_large(open('hapmap10_auto.gp')).loci_list))
print(len(read_large(open('hapmap10_auto_noofs_ld.gp')).loci_list))'''