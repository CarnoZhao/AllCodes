library(mvtnorm)

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
#with(d, plot(X1, X2, pch = ifelse(y == 1, 20, 1)))

mu.pos.hat = colMeans(d[y == 1, 1:2])
mu.neg.hat = colMeans(d[y == -1, 1:2])
Sigma.pos.hat = (t(d[y == 1, 1:2]) - mu.pos.hat) %*% t(t(d[y == 1, 1:2]) - mu.pos.hat) / nrow(d[y == 1,])
Sigma.neg.hat = (t(d[y == -1, 1:2]) - mu.neg.hat) %*% t(t(d[y == -1, 1:2]) - mu.neg.hat) / nrow(d[y == -1,])

classify = function(x.new, y){
	p.pos = dmvnorm(x.new, mu.pos.hat, Sigma.pos.hat)
	p.neg = dmvnorm(x.new, mu.neg.hat, Sigma.neg.hat)
	return(ifelse(p.pos > p.neg, 1, -1))
}

loss = sum(abs(d$y - classify(d[,1:2], d$y))) / nrow(d)
print(loss)

with(d, plot(X1, X2, pch = ifelse(y == 1, 20, 1), col = ifelse(y == classify(d[,1:2], d$y), "black", "red")))
x1.min = min(d$X1)
x1.max = max(d$X1)
x2.min = min(d$X2)
x2.max = max(d$X2)

points = sapply(
	seq(x1.min, x1.max, length.out = 500), 
	function(x1){
		x_1 = x1
		fn = function(x_2){
				x.new = c(x_1, x_2)
				p.pos = dmvnorm(x.new, mu.pos.hat, Sigma.pos.hat)
				p.neg = dmvnorm(x.new, mu.neg.hat, Sigma.neg.hat)
				(p.pos - p.neg) ^ 2
			}
		optim.out = optimize(fn, c(x2.min, x2.max))
		c(x1, optim.out$minimum)
	}
)
print(points)
lines(points[1,], points[2,])