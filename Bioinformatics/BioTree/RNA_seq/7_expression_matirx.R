pdf('heatmap.pdf')

path = '../../../../Grocery/DataSet/RNA_seq/feature_counts/all.counts'

d = read.table(path,
			  sep = "\t",
			  header = TRUE)
exprSet = d[,7:10]
meta = d[,1:6]
rownames(exprSet) = d[,1]
colnames(exprSet) = c('ctrl1', 'ctrl2', 'treat1', 'treat2')
group.list = ifelse(grepl('ctrl', colnames(exprSet)), 'ctrl', 'treat')

# hc = hclust(dist(t(exprSet)))
# plot(hc)
if(FALSE) {
		# code from GEO analysis
		notZeroRows = rownames(exprSet)[rowSums(exprSet) != 0]
		exprSet = exprSet[notZeroRows,]


		suppressPackageStartupMessages(library(limma))

		classification.matrix = model.matrix(~0 + factor(group.list))
		colnames(classification.matrix) = levels(factor(group.list))
		rownames(classification.matrix) = colnames(exprSet)

		contrast.matrix = makeContrasts(paste0(unique(group.list), collapse = '-'), levels = classification.matrix)

		fit = lmFit(exprSet, classification.matrix)

		fit2 = contrasts.fit(fit, contrast.matrix)
		fit2 = eBayes(fit2)

		tempOutput = topTable(fit2, coef = 1, n = Inf)
		nrDEG = na.omit(tempOutput)

		plot(nrDEG$logFC, -log10(nrDEG$P.Value))
}

if(TRUE){
		# new code
		suppressPackageStartupMessages(library(DESeq2))
		colData = data.frame(row.names = colnames(exprSet), group.list = group.list)
		dds = DESeqDataSetFromMatrix(countData = exprSet,
									 colData = colData,
									 design = ~ group.list)
		dds = DESeq(dds)
		res = results(dds, 
					  contrast = c('group.list', 'treat', 'ctrl'))
		resOrdered = res[order(res$padj),]
		nrDEG = as.data.frame(resOrdered)
		nrDEG = na.omit(nrDEG)

		plot(nrDEG$log2FoldChange, -log10(nrDEG$pvalue))
}

library(pheatmap)

choose.gene = head(rownames(nrDEG), 500)

choose.matrix = exprSet[choose.gene,]
choose.matrix = t(scale(t(choose.matrix)))
pheatmap(choose.matrix)


dev.off()
