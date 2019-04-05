from Bio.PopGen.GenePop import Controller as gpc
import numpy as np
import seaborn as sns
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
ctrl = gpc.GenePopController()
my_pops = [l.rstrip() for l in open('hapmap10_auto_noofs_ld.pops')]
num_pop = len(my_pops)
'''(multi_fis, multi_fst, multi_fit), f_iter = ctrl.calc_fst_all('hapmap10_auto_noofs_2')
print(multi_fis, multi_fst, multi_fit)
fst_vals = []
fis_vals = []
fit_vals = []
for f_case in f_iter:
	name, fis, fst, fit, qinter, qintra = f_case
	fis_vals.append(fis)
	fst_vals.append(fst)
	fit_vals.append(fit)

sns.set_style("whitegrid")
fig = plt.figure()
ax = fig.add_subplot(111)
ax.hist(fst_vals, 50, color = 'r')
ax.set_title('F_ST, F_IS and F_IT distributions')
ax.set_xlabel('F_ST')
ax = fig.add_subplot(222)
data = pandas.DataFrame({'fis': fis_vals, 'fit':fit_vals})
sns.violinplot(data, ax = ax, orient = "h") # Wrong
ax.set_yticklabels(['F_IS', 'F_IT'])
ax.set_xlim(-.1, 0.4)
plt.savefig('P107.png')'''

fpair_iter, avg = ctrl.calc_fst_pair('hapmap10_auto_noofs_2')
del avg
'''min_pair = min(avg.values())
max_pair = max(avg.values())
arr = np.ones((num_pop - 1, num_pop - 1, 3), dtype = float)
sns.set_style('white')
fig = plt.figure(figsize = (16, 9))
ax = fig.add_subplot(111)
for row in range(num_pop - 1):
	for column in range(row + 1, num_pop):
		val = avg[(column, row)]
		norm_val = (val - min_pair) / (max_pair - min_pair)
		ax.text(column - 1, row, '%.3f' % val, ha = 'center')
		if norm_val == 0:
			arr[row, column - 1, 0] = 1
			arr[row, column - 1, 1] = 1
			arr[row, column - 1, 2] = 0
		elif norm_val == 1:
			arr[row, column - 1, 0] = 1
			arr[row, column - 1, 1] = 0
			arr[row, column - 1, 2] = 1
		else:
			arr[row, column - 1, 0] = 1 - norm_val
			arr[row, column - 1, 1] = 1
			arr[row, column - 1, 2] = 1

ax.imshow(arr, interpolation = 'none')
ax.set_xticks(range(num_pop - 1))
ax.set_yticks(range(num_pop - 1))
ax.set_xticklabels(my_pops[1:])
ax.set_yticklabels(my_pops[:-1])
plt.savefig('P107_1.png')'''

pop_ceu = my_pops.index('CEU')
pop_yri = my_pops.index('YRI')
start_pos = 136261886
end_pos = 136350481
all_fst = []
inside_fst = []
for locus_pfst in fpair_iter:
	name = locus_pfst[0]
	pfst = locus_pfst[1]
	pos = int(name.split('/')[-1])
	my_fst = pfst[(pop_yri, pop_ceu)]
	if my_fst == '-':
		continue
	all_fst.append(my_fst)
	if pos >= start_pos and pos <= end_pos:
		inside_fst.append(my_fst)
print(inside_fst)
print('Median = %.3f, Mean = %.3f, 90%% = %.3f' % (np.median(all_fst), np.mean(all_fst), np.percentile(all_fst, 90)))