library(ggplot2)
filt = function(vec){
	ret1 = sum(vec * u1) < 0
	ret2 = sum(vec * u2) > 0
	ret3 = sum(vec * u3) < 0
	ret = ifelse(ret1 && ret2 && ret3, TRUE, FALSE)
	print(vec)
	print(c(ret1, ret2, ret3))
	return(ret)
}

prepare = function(){
	u1 = c(1, -3, 2)
	u2 = c(2, -1, 0)
	u3 = c(1, 1, -15)
	x = rep(1:10, 10)
	y = rep(1:10, each = 10)
	data = data.frame(x, y)
	label = rep(TRUE, 100)
	for (i in 1:100){
		vec = c(data[i, 1], data[i, 2], 1)
		label[i] = filt(vec)
	}
	data = cbind(data, label)
	graph = ggplot(data, mapping = aes(x = x, y = y, color = as.factor(label)))
	plot(graph + geom_point())
}

perceptron = function(data){
	dot.data = as.matrix(data[,])
}