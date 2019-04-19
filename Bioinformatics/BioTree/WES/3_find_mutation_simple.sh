samtools mpileup -ugf $genome_fa $sorted_bam | bcftools call -vmOz -o $vcf_gz

samtools index $bam


# remove PCR duplicate
samtools markdup -r $in_bam $out_bam
samtools markdup -S $in_bam $out_bam
