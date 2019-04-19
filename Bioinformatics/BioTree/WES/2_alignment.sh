bwa mem -R '...something necessary for GATK...' $index $fq1 $fq2 | samtools sort -o $bam -
# bwa mem $index $fq1 $fq2 > $sam 
# samtools sort -o $bam $sam

