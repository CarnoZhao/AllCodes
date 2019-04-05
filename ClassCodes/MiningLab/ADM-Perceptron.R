library(MASS)
library(ggplot2)
data = mvrnorm(20, c(0, 0), matrix(c(2, 0, 0, 2), 2, 2))
minpos = min(data[,1][which(data[,1] > 0)])
maxneg = max(data[,1][which(data[,1] < 0)])
data = rbind(data.frame(data, data[,1] > 0), c(rep(runif(1, 0, minpos), 2), FALSE), c(rep(runif(1, maxneg, 0), 2), TRUE))
v = as.matrix(runif(3, 0, 1))
x.data = cbind(rep(1, dim(data)[1]), as.matrix(data[,1:2]))
y.data = as.matrix((data[,3] - 0.5) * 2)	
y.est = ((x.data %*% v > 0) - 0.5) * 2
v.data = as.matrix(v)
cnt = 1
while(any(y.est != y.data)){
	v = v + t(x.data) %*% (y.data - y.est)
	y.est = ((x.data %*% v > 0) - 0.5) * 2
	v.data = cbind(v.data, v)
	cnt = cnt + 1
	if(cnt == 100){break}}
graph = ggplot(data, mapping = aes(x = X1, y = X2, color = as.factor(data[,3]))) + geom_point()
for(i in 1:dim(v.data)[2]){
	graph = graph + geom_abline(intercept = v.data[1, i], slope = -v.data[2, i] / v.data[3, i])}
plot(graph)