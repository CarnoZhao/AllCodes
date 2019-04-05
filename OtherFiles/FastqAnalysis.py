path = 'C:/Users/Carno/Desktop/1.fastq'
import gzip
with open(path) as f:
    content = f.read().split('@29154')
    seq = [read.split('\n')[1].rstrip() for read in content if read != '']
    fw = open('C:/Users/Carno/Desktop/1.txt', 'w')
    fw.write('\n'.join(seq)) 