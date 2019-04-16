for name in id; do
		prefetch $name &
done
# id is the list of sra number

for name in `ls`; do
		nohup fastq-dump --gzip --split-3 -O ./ $name &
done
