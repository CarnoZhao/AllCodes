hisat2_extract_exons.py $genome.gtf > $genome.exon
hisat2_extract_splice_sites $genome.gtf > $genome.ss

hisat2-build -p 8 $genome.fa --ss $genome.ss --exon $genome.exon $genome.index
