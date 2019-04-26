pdf('1k_genome_center_hist.pdf')
d = read.table('../CookBookData/sequence.index',
			   header = TRUE,
			   sep = '\t',
			   fill = TRUE)
library(ggplot2)
library(dplyr)

counts = summarize(group_by(d, CENTER_NAME), n = n())
graph = ggplot(counts, aes(x = CENTER_NAME, y = n)) + geom_bar(stat = 'identity')
plot(graph)
dev.off()
