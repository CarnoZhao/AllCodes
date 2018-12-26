import gffutils
import sqlite3

try:
	db = gffutils.create_db('gambiae.gff.gz', 'ag.db')
except sqlite3.OperationalError:
	db = gffutils.FeatureDB('ag.db')

from Bio import SeqIO, Alphabet, Seq
gene_id = 'AGAP004707'
gene = db[gene_id]
print(gene)
print(gene.seqid, gene.strand)

recs = SeqIO.parse('gambiae.fa', 'fasta')
for rec in recs:
	print(rec.description)
	if rec.description.split(':')[2] == gene.seqid:
		my_seq = rec.seq
		break
print(my_seq.alphabet)

def get_sequence(chrom_seq, CDSs, strand):
	seq = Seq.Seq('', alphabet = Alphabet.IUPAC.unambiguous_dna)
	for CDS in CDSs:
		my_cds = Seq.Seq(str(my_seq[CDS.start - 1: CDS.end]), alphabet = Alphabet.IUPAC.unambiguous_dna)
		seq += my_cds
	return seq if strand == '+' else seq.reverse_complement()

mRNAs = db.children(gene, featuretype = 'mRNA')
for mRNA in mRNAs:
	print(mRNA.id)
	if mRNA.id.endswith('RA'):
		break

CDSs = db.children(mRNA, featuretype = 'CDS', order_by = 'start')
gene_seq = get_sequence(my_seq, CDSs, gene.strand)

print(len(gene_seq), gene_seq)
prot = gene_seq.translate()
print(len(prot), prot)

