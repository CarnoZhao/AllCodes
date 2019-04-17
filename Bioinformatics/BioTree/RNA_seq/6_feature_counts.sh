featureCounts -T 8 -p -t exon -g gene_id -a $gtf_gz -o $feature_counts $bam
