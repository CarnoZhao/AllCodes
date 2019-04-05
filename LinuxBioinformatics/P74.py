import gffutils
import sqlite3

try:
	db = gffutils.create_db('gambiae.gff.gz', 'ag.db')
except sqlite3.OperationalError:
	db = gffutils.FeatureDB('ag.db')

print("\nPART 1:")
print(list(db.featuretypes()))

print("\nPART 2:")
for feat_type in db.featuretypes():
	print(feat_type, db.count_features_of_type(feat_type))

print("\nPART 3:")
for contig in db.features_of_type('contig'):
	print(contig)

from collections import defaultdict
num_mRNAs = defaultdict(int)
num_exons = defaultdict(int)
max_exons = 0
max_span = 0

print("\nPART 4:")
for contig in db.features_of_type('contig'):
	cnt = 0
	for gene in db.region((contig.seqid, contig.start, contig.end), featuretype = 'gene'):
		cnt += 1
		span = abs(gene.start - gene.end)
		if span > max_span:
			max_span = span
			max_span_gene = gene
		my_mRNAs = list(db.children(gene, featuretype = 'mRNA'))
		num_mRNAs[len(my_mRNAs)] += 1
		if len(my_mRNAs) == 0:
			exon_check = [gene]
		else:
			exon_check = my_mRNAs
		for check in exon_check:
			my_exons = list(db.children(check, featuretype = 'exon'))
			num_exons[len(my_exons)] += 1
			if len(my_exons) > max_exons:
				max_exons = len(my_exons)
				max_exon_gene = gene
	print('contig %s, number of genes %d' % (contig.seqid, cnt))

print("\nPART 5:")
print('Max number of exons: %s (%d)' % (max_exon_gene.id, max_exons))
print('Max span: %s (%d)' % (max_span_gene.id, max_span))
print(num_mRNAs)
print(num_exons)