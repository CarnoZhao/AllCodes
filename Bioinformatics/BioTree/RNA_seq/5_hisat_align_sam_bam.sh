hisat2 -p 8 -x $index -1 $fq1 -2 $fq2 -S $sam
samtools sort -O bam
for name in `ls`
do
		samtools view -b -S $sam > $bam
		samtools sort -o $sorted_bam $bam
		samtools index $sorted_bam
		samtools flagstat $sorted_bam > $bam_flagstat
done

