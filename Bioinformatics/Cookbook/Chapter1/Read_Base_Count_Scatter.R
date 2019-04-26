library(ggplot2)

pdf('Read_Base_Count_Scatter.pdf')
d = read.table('../CookBookData/sequence.index',
			   header = TRUE,
			   sep = '\t',
			   fill = TRUE)
d$BASE_COUNT = sapply(d$BASE_COUNT, as.integer)
d$READ_COUNT = sapply(d$READ_COUNT, as.integer)

d = d[d$POPULATION %in% c('YRI', 'CEU') & d$BASE_COUNT < 2E9 & d$READ_COUNT < 3E7, c('POPULATION', 'BASE_COUNT', 'READ_COUNT', 'ANALYSIS_GROUP')]
graph = ggplot(d, aes(x = BASE_COUNT, y = READ_COUNT, shape = POPULATION, color = ANALYSIS_GROUP)) + geom_point() + xlim(c(0, 2E9)) + ylim(c(0, 3E7))
plot(graph)
dev.off()
