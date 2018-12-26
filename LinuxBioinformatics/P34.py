from Bio import SeqIO
import seaborn as sns
import matplotlib.pyplot as plt
from collections import defaultdict

recs = SeqIO.parse('SRR003265.filt.fastq', 'fastq')
qual_pos = defaultdict(list)

for rec in recs:
    for i, qual in enumerate(rec.letter_annotations['phred_quality']):
        if i < 25 or qual == 40:
            continue
        pos = i + 1
        qual_pos[pos].append(qual)

vps = []
poses = list(qual_pos.keys())
poses.sort()

for pos in poses:
    vps.append(qual_pos[pos])

fig, ax = plt.subplots()
sns.boxplot(data = vps, ax = ax)
ax.set_xticklabels([str(x) for x in range(26, max(qual_pos.keys()) + 1)])

plt.show()
