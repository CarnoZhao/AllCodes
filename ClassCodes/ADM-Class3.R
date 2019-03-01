library(mvtnorm)
library(ggplot2)

n.pos = 500
n.neg = 500
dimention = 2
mu.pos = c(-1, 2)
mu.neg = c(2, -1)
Sigma.pos = diag(1, 2)
Sigma.neg = matrix(c(1.25, 0, 0, 2), nrow = 2)

x.pos = rmvnorm(n.pos, mu.pos, Sigma.pos)
x.neg = rmvnorm(n.neg, mu.neg, Sigma.neg)
y = c(rep(1, n.pos), rep(-1, n.neg))
d = data.frame(rbind(x.pos, x.neg), y)
graph = ggplot(d, aes(x = X1, y = X2, color = as.factor(y))) + geom_point()

mu.pos.hat = colMeans(d[y == 1, 1:2])
mu.neg.hat = colMeans(d[y == -1, 1:2])
Sigma.pos.hat = (t(d[y == 1, 1:2]) - mu.pos.hat) %*% t(t(d[y == 1, 1:2]) - mu.pos.hat) / nrow(d[y == 1,])
Sigma.neg.hat = (t(d[y == -1, 1:2]) - mu.neg.hat) %*% t(t(d[y == -1, 1:2]) - mu.neg.hat) / nrow(d[y == -1,])

x.new = runif(2)
p.pos = dmvnorm(x.new, mu.pos.hat, Sigma.pos.hat)
p.neg = dmvnorm(x.new, mu.neg.hat, Sigma.neg.hat)
y.new = ifelse(p.pos > p.neg, 1, -1)
plot(graph)