pdf('GEO_1.pdf')
# suppressPackageStartupMessages(library(GEOquery))
suppressPackageStartupMessages(library(hugene10sttranscriptcluster.db))
library(ggplot2)
# Different platforms use different packages 

# gset = getGEO('GSE42872', destdir = './data', 
# 			  AnnotGPL = FALSE, 
# 			  getGPL = FALSE)
a = read.table('./data/GSE42872_series_matrix.txt.gz', 
		sep = '\t',
		quote = "",
		fill = T,
 		comment.char = '!',
		header = TRUE)
rownames(a) = a[,1]
a = a[,-1]

# a = exprs(gset[[1]])
# columns are samples, rows are genes

ids = toTable(hugene10sttranscriptclusterSYMBOL)

exprSet = a
table(rownames(exprSet) %in% ids$probe_id)
# how many genes are in the ids
exprSet = exprSet[rownames(exprSet) %in% ids$probe_id,]
# remove all the genes that are not in ids

ids = ids[match(ids$probe_id, rownames(exprSet)),]
# sort ids to fit exprSet

# newexSet = exprSet[ids[,2] == 'IGKC',]
# choose a gene to get the genes's expression 
tmp = by(exprSet,
		 ids$symbol,
		 function(x){
		 	rownames(x)[which.max(rowMeans(x))]
		 })
probes = as.character(tmp)
newexSet = exprSet[rownames(exprSet) %in% probes,]
colnames(newexSet) = c('vehicle.1', 'vehicle.2', 'vehicle.3', 'remurafenib.1', 'remurafenib.2', 'remurafenib.3') 
# rownames(newexSet) = sapply(rownames(newexSet), function(x){
# 		 ids[ids$probe_id == x, 2]})
# write.csv(newexSet, file = './data/GSE42872_clean.csv')
newexSet$probe = sapply(rownames(newexSet), function(x){
		 ids[ids$probe_id == x, 2]})
# newexSet['GAPDH',]
# newexSet['ACTB',]
# there are two of the high-expression genes

group.list = rep(c(rep('vehicle', 3), rep('remurafenib', 3)), each = nrow(newexSet))

# boxplot
library(reshape2)
newexSet.melt = melt(newexSet)
colnames(newexSet.melt) = c('probe', 'sample', 'value')
newexSet.melt$group = group.list
graph = ggplot(newexSet.melt, aes(x = sample, y = value, fill = as.factor(group))) + geom_boxplot()
plot(graph)

# evolutionary graph
hc = hclust(dist(t(newexSet[,colnames(newexSet) != 'probe'])))
plot(hc)

# PCA graph
library(ggfortify)
df = as.data.frame(t(newexSet[,colnames(newexSet) != 'probe']))
df$group = c(rep('vehicle', 3), rep('remurafenib', 3))
autoplot(prcomp(df[,1:(ncol(df) - 1)]), data = df, colour = 'group')

dev.off();
