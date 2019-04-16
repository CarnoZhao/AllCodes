path='/mnt/d/OneDrive - mails.ucas.edu.cn/DataSet/RNA_seq'



trim_glore -q 25 --phred33 --length 50 -e 0.1 --stringency 3 --paired -o $dir $fq1 $fq2
