pdf('GEO_3.pdf')
exprsSet = read.table('./data/GSE42872_clean.csv', row.name = 1, header = TRUE, sep = ',')
nrDEG = read.table('./data/difference_analysis.csv', row.name = 1, header = TRUE, sep = ',')
group.list = rep(c('control', 'case'), each = 3)

library(clusterProfiler)

gene = head(rownames(nrDEG), 1000)
gene.df = bitr(gene, fromType = 'SYMBOL', toType = c('ENSEMBLE', 'ENTREZID'), OrgDB = org.Hs.eg.db)
head(gene.df)

kk = enrichKEGG(gene = gene,
				organism = 'hsa',
				pvalueCutoff = 0.05)

dev.off();
