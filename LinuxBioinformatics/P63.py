from __future__ import print_function
from __future__ import division
from Bio import SeqIO
genome_name = 'PlasmoDB-9.3_Pfalciparum3D7_Genome.fasta'
recs = SeqIO.parse(genome_name, 'fasta')
for rec in recs:
	print(rec.description)

from Bio import SeqUtils

chrom_sizes = {}
chrom_GC = {}
block_size = 50000
min_GC = 100.0
max_GC = 0.0
recs = SeqIO.parse(genome_name, 'fasta')
for rec in recs:
	if rec.description.find('SO=chromosome') == -1:
		continue
	chrom = int(rec.description.split('_')[1])
	chrom_GC[chrom] = []
	size = len(rec.seq)
	chrom_sizes[chrom] = size
	num_blocks = size // block_size + 1
	for block in range(num_blocks):
		start = block_size * block
		if block == num_blocks - 1:
			end = size
		else:
			end = block_size + start + 1
		block_seq = rec.seq[start: end]
		block_GC = SeqUtils.GC(block_seq)
		if block_GC < min_GC:
			min_GC = block_GC
		if block_GC > max_GC:
			max_GC = block_GC
		chrom_GC[chrom].append(block_GC)
	print(min_GC, max_GC)

from reportlab.lib import colors
from reportlab.lib.units import cm
from Bio.Graphics import BasicChromosome

chroms = list(chrom_sizes.keys())
chroms.sort()
biggest_chrom = max(chrom_sizes.values())
my_genome = BasicChromosome.Organism(output_format = 'png')
my_genome.page_size = (29.7 * cm, 21 * cm)
telomere_length = 10
bottom_GC = 17.5
top_GC = 22.0
for chrom in chroms:
	chrom_size = chrom_sizes[chrom]
	chrom_representation = BasicChromosome.Chromosome \
		('Cr%d' % chrom)
	chrom_representation.scale_num = biggest_chrom
	tel = BasicChromosome.TelomereSegment()
	chrom_representation.add(tel)
	num_blocks = len(chrom_GC[chrom])
	for block, gc in enumerate(chrom_GC[chrom]):
		my_GC = chrom_GC[chrom][block]
		body = BasicChromosome.ChromosomeSegment()
		if my_GC > top_GC:
			body.fill_color = colors.Color(1, 0, 0)
		elif my_GC < bottom_GC:
			body.fill_color = colors.Color(1, 1, 0)
		else:
			my_color = (my_GC - bottom_GC) / (top_GC - bottom_GC)
			body.fill_color = colors.Color(my_color, my_color, 1)
		if block < num_blocks - 1:
			body.scale = block_size
		else:
			body.scale = chrom_size % block_size
		chrom_representation.add(body)
	tel = BasicChromosome.TelomereSegment(inverted = True)
	tel.scale = telomere_length
	chrom_representation.add(tel)
	my_genome.add(chrom_representation)

my_genome.draw('falciparum.png', 'Plasodium falciparum')
