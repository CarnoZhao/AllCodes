pdf('GEO_4.pdf')
# data(geneList, package = 'DOSE')
suppressPackageStartupMessages(library(clusterProfiler))

nrDEG = read.table('./data/difference_analysis.csv', row.name = 1, header = TRUE, sep = ',')

suppressPackageStartupMessages(library(org.Hs.eg.db))
geneList= bitr(rownames(nrDEG), fromType = 'SYMBOL', toType = 'ENTREZID', OrgDb = org.Hs.eg.db)
geneList$logFC = nrDEG[geneList$SYMBOL,'logFC']
names = geneList$ENTREZID
geneList = geneList[,'logFC']
names(geneList) = names
geneList = sort(geneList, decreasing = TRUE)
head(geneList)

kk2 = gseKEGG(geneList = geneList,
			  organism = 'hsa',
			  nPerm = 1000,
			  minGSSize = 120,
			  pvalueCutoff = 0.05,
			  verbose = FALSE)
head(kk2[,1:6])
gseaplot(kk2, geneSetID = 'hsa04145')

dev.off()
