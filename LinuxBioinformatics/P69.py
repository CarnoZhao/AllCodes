import gzip
from Bio import SeqIO
gambiae_name = 'gambiae.fa.gz'
recs = SeqIO.parse('gambiae.fa', 'fasta')
chrom_Ns = {}
chrom_sizes = {}
for rec in recs:
	print(rec.description)
	chrom = rec.description.split(":")[2]
	if chrom in ['UNKN', 'Y_unplaced']:
		continue
	chrom_Ns[chrom] = []
	on_N = False
	curr_size = 0
	for n in rec.seq:
		if n in ['N', 'n']:
			curr_size += 1
			on_N = True
		else:
			if on_N:
				chrom_Ns[chrom].append(curr_size)
				curr_size = 0
			on_N = False
	if on_N:
		chrom_Ns[chrom].append(curr_size)
	chrom_sizes[chrom] = len(rec.seq)
for chrom, Ns in chrom_Ns.items():
	size = chrom_sizes[chrom]
	print('%s (%s): %%Ns (%.1f), num Ns: %d, max N: %d' % \
		(chrom, size, 100 * sum(Ns) / size, len(Ns), max(Ns)))
