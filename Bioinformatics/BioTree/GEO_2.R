pdf('GEO_2.pdf')
exprSet = read.table('./data/GSE42872_clean.csv', sep = ',', row.name = 1, header = TRUE)
group.list = c(rep('control', 3), rep('case', 3))
library(limma)


# classification matrix
design = model.matrix(~0 + factor(group.list))
colnames(design) = levels(factor(group.list))
rownames(design) = colnames(exprSet)

# contrast matrix
contrast.matrix = makeContrasts(paste0(unique(group.list), collapse = '-'), levels = design)

fit = lmFit(exprSet, design)

fit2 = contrasts.fit(fit, contrast.matrix)
fit2 = eBayes(fit2)

tempOutput = topTable(fit2, coef = 1, n = Inf)
nrDEG = na.omit(tempOutput)
# write.csv(nrDEG, file = './data/difference_analysis.csv')
# summary of gene expression difference

# heat map
library(pheatmap)
choose.gene = head(rownames(nrDEG), 25)
# choose.gene = rownames(nrDEG)
choose.matrix = exprSet[choose.gene,]
choose.matrix = t(scale(t(choose.matrix)))
pheatmap(choose.matrix)

# volcano graph
plot(nrDEG$logFC, -log10(nrDEG$P.Value))


dev.off();
