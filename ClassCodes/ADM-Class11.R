n = 200 # sample size
d = 2 # features
x = matrix(runif(n * d, -10, 10), nrow = n)
v = runif(d, -1, 1)
c = runif(1)
prob = plogis(x %*% v - c)
y = rbinom(n, 1, prob = prob)
library(ggplot2)
d = data.frame(x, y)
X1 = d$X1
X2 = d$X2
graph = ggplot(d, aes(x = X1, y = X2, color = as.factor(y))) + geom_point()
mf = model.frame(y ~ -1 + X1 + X2, d)
data = list(x = model.matrix(mf), y = model.response(mf))


f = function(par, y, x){
	v = par[-length(par)]
	c = par[length(par)]
	ret = -sum(y * log(plogis(x %*% v - c)) + (1 - y) * log(1 - plogis(x %*% v - c)))
	return(ret)
}

par.random = runif(d, -1, 1)
optimFit = optim(par.random, f, y = y, x = x)
par = optimFit$par

glmFit = glm(y ~ X1 + X2, d, family = binomial)

g = function(par, y, x){
	v = par[-length(par)]
	c = par[length(par)]
	return(t(cbind(x, -1)) %*% (plogis(x %*% v - c) - y))
}

optimFit.g = optim(par.random, f, gr = g, y = y, x = x, method = "BFGS")

f.svm = function(par, y, x, t) {
	v = par[-length(par)]
	c = par[length(par)]

	lin.pred = x %*% v - c
	y = 2 * (y - 1)

	return(mean(pmax(0, 1 - y * lin.pred)) + t * sum(v ^ 2))
}

optimFit.svm  = optim(par.random, f.svm, y = y, x = x, t = 1)
par.svm = optimFit.svm$par * 100
print(par.svm)
#graph = graph + geom_abline(intercept = par[3] / par[2], 
#			slope = -par[1] / par[2], color = 'red')
#graph = graph + geom_abline(intercept = c / v[2], 
#			slope = -v[1] / v[2], color = 'green')
graph = graph + geom_abline(intercept = par.svm[3] / par.svm[2], 
			slope = -par.svm[1] / par.svm[2], color = 'red')
plot(graph)