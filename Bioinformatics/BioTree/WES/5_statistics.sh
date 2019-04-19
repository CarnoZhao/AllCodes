samtools index $bam
samtools flagstat $bam > $bam_stat
qualimap bamqc --java-mem-size=8G -gff $exon_bed $name
