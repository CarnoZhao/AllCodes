gatk --java-options "-Xmx20G -Djava.io.tmpdir=./" \
		Markduplicates \
		-I $bam \
		-O $marked_bam \
		-M $name_matrix 


gatk --java-options "-Xmx20G -Djava.io.tmpdir=./" \
		FixMateInformation \
		-I $marked_bam \
		-O $marked_fixed_bam \
		-SO coordiante

samtools index $marked_fixed_bam

gatk --java-options "-Xmx20G -Djava.io.tmpdir=./" \
		BaseRecalibrator \
		-R $ref_genome \
		-I $marked_fixed_bam \
		--known-sites $snp_from_gatk \
		--known-sites $indel_from_gatk \
		-O $name_recal_table

gatk --java-options "-Xmx20G -Djava.io.tmpdir=./" \
		ApplyBQSR \
		-R $ref_genome \
		-I $marked_fixed_bam \
		-bqsr $name_recal_table \
		-O $bqsr_bam

gatk --java-options "-Xmx20G -Djava.io.tmpdir=./" \
		HaplotypeCaller \
		-R $ref_genome \
		-I $bqsr_bam \
		--dbsnp $snp_from_gatk \
		-O $name_raw_vcf
