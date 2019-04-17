hisat2 -p 8 -x $index -1 $fq1 -2 $fq2 -S $sam
samtools sort -O bam
for name in `ls`
do
		samtools sort -O bam -@ 5 -o $bam $sam
done
samtools index $bam
