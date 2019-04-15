library(ggplot2)
x = 1:10
y = x ^ 2
pdf('Rplots.pdf')
graph = ggplot(data.frame(x, y), aes(x = x, y = y)) + geom_point()
plot(x, x ^ 3)
plot(graph)
dev.off();

