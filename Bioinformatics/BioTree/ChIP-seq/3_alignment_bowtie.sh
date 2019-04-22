bowtie2 -p 5 -x $genome_bt2 -U $fq_gz -S $file_sam
samtools view -b $file_sam > $file_bam
samtools sort $file_bam -o $file_sorted_bam
samtools index $file_sorted_bam
