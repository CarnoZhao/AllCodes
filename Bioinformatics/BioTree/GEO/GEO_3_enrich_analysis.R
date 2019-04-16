pdf('GEO_3.pdf')
exprsSet = read.table('./data/GSE42872_clean.csv', row.name = 1, header = TRUE, sep = ',')
nrDEG = read.table('./data/difference_analysis.csv', row.name = 1, header = TRUE, sep = ',')
group.list = rep(c('control', 'case'), each = 3)

suppressPackageStartupMessages(library(clusterProfiler))
# suppressPackageStartupMessages(library(org.Hs.eg.db))

# gene = head(rownames(nrDEG), 1000)
# gene.df = bitr(gene, fromType = 'SYMBOL', toType = c('ENSEMBL', 'ENTREZID'), OrgDb = org.Hs.eg.db)
# write.csv(gene.df, file = './data/Ensembl_EntrezID.csv')
gene.df = read.table('./data/Ensembl_EntrezID.csv', row.name = 1, header = TRUE, sep = ',')

kk = enrichKEGG(gene = gene.df$ENTREZID,
				organism = 'hsa',
				pvalueCutoff = 0.05)
head(kk[,1:6])
# sorted by p-value
# the smaller p-value is, the more likely the genes with different expression are significantly related to this biological pathway(KEGG)
# enrichGO, gseGO, gseKEGG
# write.csv(kk, file = './data/KEGG_enrich.csv')


dev.off();
