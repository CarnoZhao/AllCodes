path="/mnt/d/OneDrive - mails.ucas.edu.cn/DataSet/RNA_seq/"
mkdir -p $path'fastqcResult'
for name in `ls $path | grep '.fq.gz'`; do
		fastqc $name -t 8 -o $path'fastqcResult'
done

multiqc $path'fastqcResult'
