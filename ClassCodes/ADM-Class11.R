RandomExample = function(){
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
	#data = list(x = model.matrix(mf), y = model.response(mf))

	par.random = runif(d, -1, 1)
	optimFit = optim(par.random, f, y = y, x = x)
	par = optimFit$par
	optimFit.g = optim(par.random, f, gr = g, y = y, x = x, method = "BFGS")
	glmFit = glm(y ~ X1 + X2, d, family = binomial)
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
}

f = function(par, y, x){
	v = par[-length(par)]
	c = par[length(par)]
	ret = -sum(y * log(plogis(x %*% v - c)) + (1 - y) * log(1 - plogis(x %*% v - c)))
	return(ret)
}

g = function(par, y, x){
	v = par[-length(par)]
	c = par[length(par)]
	return(t(cbind(x, -1)) %*% (plogis(x %*% v - c) - y))
}

f.svm = function(par, y, x, t) {
	v = par[-length(par)]
	c = par[length(par)]

	lin.pred = x %*% v - c
	y = 2 * (y - 1)

	return(mean(pmax(0, 1 - y * lin.pred)) + t * sum(v ^ 2))
}

RealExample = function() {
	n = 200
	d = 4
	female = rbinom(n, 1, 0.51)
	age = ifelse(female == 1,
		floor(rgamma(n, 15, 0.5) + 35),
		floor(rgamma(n, 18, 0.6) + 35))
	theta.u = c(qlogis(0.2), 0.15, 0.1)
	prob = plogis(cbind(1, (age - mean(age)) / sd(age), female) %*% theta.u)
	history = rbinom(n, 1, prob)
	theta.z = c(qlogis(0.05), 0.1, 0, 0.75)
	prob = plogis(cbind(1, (age - mean(age)) / sd(age), female, history) %*% theta.z)
	drug = rbinom(n, 1, prob)
	theta.y = c(qlogis(0.1), 0.1, -0.025, 0.75, 0.2)
	prob = plogis(cbind(1, (age - mean(age)) / sd(age), female, history, drug) %*% theta.y)
	rash = rbinom(n, 1, prob)
	df = data.frame(age, female, history, drug, rash)
	mf = model.frame(rash ~ age + female + history + drug, df)
	y = as.integer(rash)
	x = as.matrix(cbind(age, female, history, drug))
	data = list(y = y, x = x)

	print('optimResult.glm.f')
	optimResult.glm.f = optim(rep(0, 5), f, y = data$y, x = data$x)
	print(optimResult.glm.f$par)
	print('')
	print('glmFit')
	print('')
	glmFit = glm(rash ~ age + female + history + drug, df, family = binomial)
	print(as.numeric(glmFit$coefficients))
	print('')
	print('optimResult.glm.g')
	optimResult.glm.g = optim(rep(0, 5), f, gr = g, y = data$y, x = data$x, method = 'BFGS')
	print(optimResult.glm.g$par)
	print('')
	print('optimResult.svm')
	optimResult.svm = optim(rep(0, 5), f.svm, y = data$y, x = data$x, t = 1)
	print(optimResult.svm$par)
	print('')
	print('svmFit')
	library(e1071)
	svmFit = svm(rash ~ age + female + history + drug, df, type = 'C-classification', kernel = 'linear', cost = 1)
	v.svm = crossprod(svmFit$SV, svmFit$coefs)
	print(as.numeric(v.svm))
	plot(data$x %*% optimResult.svm$par[1:4], data$x %*% v.svm, pch = 20)
}

RealExample()