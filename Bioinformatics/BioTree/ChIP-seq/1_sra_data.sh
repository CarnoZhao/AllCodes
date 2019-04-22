# get the accession list
prefetch $sra_num

fasterq-dump -p -e 8 -3 -o $fq $sra_num

gzip $fq

# get the name table from sra dataset
cat $name_table | less -SN | cut -f4 | awk '{if(NR%2==0 && NR!=1) print $0"_1"; else if(NR!=1) print $0"_2"}' > col1.txt
cat $name_table | less -SN | cut -f8 | awk '{if(NR!=1) print $0}' > col2.txt
paste col1.txt col2.txt > $name_txt

cat $name_txt | while read row; do
	arr=(${=row})
	srr=$row[2]
	sample=$row[1]
	mv $srr".fq.gz" $sample".fq.gz"
done

fastqc $fq_gz
multiqc ./
