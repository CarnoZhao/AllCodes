path=/mnt/d/Grocery/DataSet/RNA_seq

dir=$path/trimResult

mkdir -p $dir

for name in `ls $path | grep hela | cut -d '_' -f1-3 | uniq`
do
		fq1=$path"/"$name"_R1.fq.gz"
		fq2=$path"/"$name"_R2.fq.gz"
		trim_galore -q 25 --phred33 --length 50 -e 0.1 --stringency 3 --paired -o $dir $fq1 $fq2
done
