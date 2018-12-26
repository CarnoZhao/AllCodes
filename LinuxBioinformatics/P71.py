import numpy as np
from Bio import SeqIO
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

recs = SeqIO.parse('atroparvus.fa', 'fasta')
sizes = []
size_N = []
for rec in recs:
	size = len(rec.seq)
	sizes.append(size)
	cnt_N = 0
	for nuc in rec.seq:
		if nuc in ['N', 'n']:
			cnt_N += 1
	size_N.append((size, cnt_N / size))
print(len(sizes), min(sizes), np.percentile(sizes, 10), np.median(sizes), \
	np.mean(sizes), np.percentile(sizes, 90), max(sizes))

small_split = 4800
large_split = 540000

fig, axs = plt.subplots(1, 3, figsize = (16, 9), squeeze = False)
xs, ys = zip(*[(x, 100 * y) for x, y in size_N if x <= small_split])
axs[0, 0].plot(xs, ys, '.')
axs[0, 0].set_ylim(-0.1, 3.5)
xs, ys = zip(*[(x, 100 * y) for x, y in size_N if x > small_split and x <= large_split])
axs[0, 1].plot(xs, ys, '.')
axs[0, 1].set_xlim(small_split, large_split)
xs, ys = zip(*[(x, 100 * y) for x, y in size_N if x > small_split])
axs[0, 2].plot(xs, ys, '.')
axs[0, 0].set_ylabel('Fraction of Ns', fontsize = 12)
axs[0, 1].set_xlabel('Contig size', fontsize = 12)
fig.suptitle('Fraction of Ns per contig size', fontsize = 26)
plt.show()
plt.savefig('P71.png')
