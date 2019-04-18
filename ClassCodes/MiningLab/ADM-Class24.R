pixels = as.matrix(read.table('../Data/uspsdata.txt'))
labels = as.matrix(read.table('../Data/uspscl.txt'))

sigmoid = function(x){
		1 / (1 + exp(-x))
}

weight = function(){
		w1 = rnorm(256 * 2, 0, 1)
		dim(w1) = c(256, 2)
		w2 = rnorm(2, 0, 1)
}

forward = function(w1, w2){
		a2 = pixels %*% w1
		z2 = sigmoid(a2)
		a3 = z2 %*% w2
		z3 = sigmoid(a3)
		return(list(z2 = z2, z3 = z3))
}

backward = function(pixels, z2, z3, labels){
		dw2 = t(z2) %*% (labels - z3)
		dw1 = (labels - z3) %*% t(w2)
}
