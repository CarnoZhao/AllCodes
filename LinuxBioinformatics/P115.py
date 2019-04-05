f = open('relationships_w_pop_121708.txt')
ind_pop = {}
f.readline()
for l in f:
	toks = l.rstrip().replace(' ', '\t').split('\t')
	fam_id = toks[0]
	ind_id = toks[1]
	pop = toks[-1]
	ind_pop['/'.join([fam_id, ind_id])] = pop
f.close()
ind_pop['2469/NA20281'] = ind_pop['2805/NA20281']

f = open('hapmap10_auto_noofs_ld_12.ped')
ninds = 0
ind_order = []
for l in f:
	ninds += 1
	toks = l[:100].replace(' ', '\t').split('\t')
	fam_id = toks[0]
	ind_id = toks[1]
	ind_order.append('%s/%s' % (fam_id, ind_id))
nsnps = (len(l.replace(' ', '\t').split('\t')) - 6) // 2
f.close()

import numpy as np
pca_array = np.empty((ninds, nsnps), dtype = int)
f = open('hapmap10_auto_noofs_ld_12.ped')
for ind, l in enumerate(f):
	snps = l.replace(' ', '\t').split('\t')[6:]
	for pos in range(len(snps) // 2):
		a1 = int(snps[2 * pos])
		a2 = int(snps[2 * pos + 1])
		my_code = a1 + a2 - 2
		pca_array[ind, pos] = my_code
f.close()

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
my_pca = PCA(n_components = 8)
my_pca.fit(pca_array)
trans = my_pca.transform(pca_array)

from genomics.popgen.pca import plot
sc_ind_comp = {}
for i, ind_pca in enumerate(trans):
	sc_ind_comp[ind_order[i]] = ind_pca
fig = plt.figure()
fig, ax = plot.render_pca_eight(sc_ind_comp, cluster = ind_pop)
plt.savefig('P115.png')