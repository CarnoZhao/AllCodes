# annovar

# align based on gene
convert2annovar.pl -format vcf4fold $vcf > $name_annovar
# ^ extract some information
annotate_variation.pl -buildver hg38 --geneanno --outfile $name_anno $name_annovar $path_to_annovar_genome_db
# annotation output files


# align based on position

# align based on data base 
