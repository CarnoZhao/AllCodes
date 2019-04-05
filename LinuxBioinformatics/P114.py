f = open('relationships_w_pop_121708.txt')
ind_pop = {}
f.readline()
for l in f:
	toks = l.rstrip().split('\t')
	fam_id = toks[0]
	ind_id = toks[1]
	pop = toks[-1]
	ind_pop['/'.join([fam_id, ind_id])] = pop

f.close()
ind_pop['2469/NA20281'] = ind_pop['2805/NA20281']

'''from genomics.popgen.plink.convert import to_eigen
to_eigen('hapmap10_auto_noofs_ld_12', 'hapmap10_auto_noofs_ld_12')'''

from genomics.popgen.pca import smart
import os
file_name = 'hapmap10_auto_noofs_ld_12'
params = "-p {0}.plot -l {0}.log -i {0}.geno -a {0}.snp -b {0}.ind -o {0} -m 0 -e {0}.eval".format(file_name)
os.system('smartpca %s' % params)
wei, wei_perc, ind_comp = smart.parse_evec('hapmap10_auto_noofs_ld_12.evec', 'hapmap10_auto_noofs_ld_12.eval')
del wei
del wei_perc
from genomics.popgen.pca import plot
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
fig = plt.figure()
fig, ax = plot.render_pca(ind_comp, 1, 2, cluster = ind_pop)
plt.savefig('P114.png')