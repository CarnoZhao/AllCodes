main1 = function(){
	library(MASS)
	library(ggplot2)
	data = mvrnorm(20, c(0, 0), matrix(c(2, 0, 0, 2), 2, 2))
	#minpos = min(data[,1][which(data[,1] > 0)])
	#maxneg = max(data[,1][which(data[,1] < 0)])
	#data = rbind(data.frame(data, data[,1] > 0), c(rep(runif(1, 0, minpos), 2), FALSE),c(rep(runif(1, maxneg, 0), 2), TRUE))
	data = data.frame(data, data[,1] > 0)
	v = as.matrix(runif(3, 0, 1))
	x.data = cbind(rep(1, dim(data)[1]), as.matrix(data[,1:2]))
	y.data = as.matrix((data[,3] - 0.5) * 2)	
	y.est = ((x.data %*% v > 0) - 0.5) * 2
	v.data = as.matrix(v)
	cnt = 1
	print(y.data)
	while(any(y.est != y.data)){
		v = v + t(x.data) %*% (y.data - y.est)
		y.est = ((x.data %*% v > 0) - 0.5) * 2
		print(y.est)
		v.data = cbind(v.data, v)
		cnt = cnt + 1
		if(cnt == 1000){break}}
	graph = ggplot(data, mapping = aes(x = X1, y = X2, 
		color = as.factor(data[,3]))) + geom_point()
	graph.points = graph
	for(i in 1:dim(v.data)[2]){
		graph = graph + geom_abline(intercept = v.data[1, i], 
			slope = -v.data[2, i] / v.data[3, i])}
	graph = graph + geom_abline(intercept = v.data[1, dim(v.data)[2]], 
			slope = -v.data[2, dim(v.data)[2]] / v.data[3, dim(v.data)[2]], color = 'red')
	plot(graph)
}

main2 = function(){
	n.pos = 75
	n.neg = 50
	d = 3

	set.seed(0)
	mu.pos = c(5, 3, 2)
	sd.pos = c(1.75, 2, 1)
	cor.pos.ij = c(0.2, -0.5, 0.3)
	cor.pos = diag(1, d)
	cor.pos[lower.tri(cor.pos)] = cor.pos.ij
	cor.pos[upper.tri(cor.pos)] = t(cor.pos)[upper.tri(cor.pos)]
	Sigma.pos = diag(sd.pos) %*% cor.pos %*% diag(sd.pos)

	mu.neg = c(2.5, 1, -2)
	sd.neg = c(1.25, 1.5, 1.25)
	cor.neg.ij = c(0.3, -0.2, 0.15)
	cor.neg = diag(1, d)
	cor.neg[lower.tri(cor.neg)] = cor.neg.ij
	cor.neg[upper.tri(cor.neg)] = t(cor.neg)[upper.tri(cor.neg)]
	Sigma.neg = diag(sd.neg) %*% cor.neg %*% diag(sd.neg)

	library(mvtnorm)
	library(rgl)
	x.pos = rmvnorm(n.pos, mu.pos, Sigma.pos)
	x.neg = rmvnorm(n.neg, mu.neg, Sigma.neg)

	df = data.frame(y = c(rep(1, n.pos), rep(-1, n.neg)), rbind(x.pos, x.neg))
	rgl_init = function(new.device = FALSE, bg = "white", width = 640){
		if (new.device || rgl.cur() == 0){
			rgl.open()
			par3d(windowRect = 50 + c(0, 0, width, width))
			rgl.bg(color = bg)
		}
		rgl.clear(type = c("shapes", "bboxdeco"))
		rgl.viewpoint(theta = 15, phi = 20, zoom = 0.7)
	}
	theta = rnorm(4)
	for (i in 1:100){
		grad = g(theta, as.vector(df$y), as.matrix(df[,2:4]))
		if(all(grad == 0)) break
		theta = theta - grad
	}
	cat("converged after ", i, " iterations\n", sep = "")
	v.h = theta[1:3]
	c = theta[4]
	v.h.norm = sqrt(sum(v.h ^ 2))
	u.h = v.h / v.h.norm
	c = c / v.h.norm
	rgl_init()

	with(df, plot3d(X1, X2, X3, type = "p", col = ifelse(y == 1, "red", "blue"), size = 5, box = FALSE, axes = TRUE))
	planes3d(u.h[1], u.h[2], u.h[3], d = -c, color = 'gray')
}

f = function(theta, y, x){
	v = theta[-length(theta)]
	c = theta[length(theta)]
	pred = as.vector(x %*% v - c)
	sum((sign(pred) != y) * abs(pred))
}

g = function(theta, y, x){
	v = theta[-length(theta)]
	c = theta[length(theta)]
	pred = as.vector(x %*% v - c)
	misc = sign(pred) != y
	if(sum(misc) == 0L){
		return(rep_len(0, length(theta)))
	}
	colSums(-y[misc] * cbind(x[misc,], -1))
}

main2()