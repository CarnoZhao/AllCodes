pixels = as.matrix(read.table('../Data/uspsdata.txt'))
labels = as.matrix(read.table('../Data/uspscl.txt'))

n1 = 256
n2 = 2
n3 = 1

sigmoid = function(x){
		1 / (1 + exp(-x))
}

weight = function(){
		w1 = rnorm((n1 + 1) * n2, 0, 1)
		dim(w1) = c(n1 + 1, n2)
		w2 = rnorm((n2 + 1) * n3, 0, 1)
		dim(w2) = c(n2 + 1, n3)
		return(list(w1 = w1, w2 = w2))
}

forward = function(pixels, w1, w2){
		z1 = cbind(rep(1, nrow(pixels)), pixels)
		a2 = z1 %*% w1
		z2 = cbind(rep(1, nrow(a2)), sigmoid(a2))
		a3 = z2 %*% w2
		z3 = sigmoid(a3)
		return(list(z1 = z1, z2 = z2, z3 = z3))
}

backward = function(z1, z2, z3, labels, w2){
		dw2 = t(z2) %*% (labels - z3)
		dw1 = t(z1) %*% ((labels - z3) %*% t(w2) * z2 * (1 - z2))
		return(list(dw1 = dw1, dw2 = dw2))
}

main = function(){
		w1_w2 = weight()
		w1 = w1_w2$w1
		w2 = w1_w2$w2
		for (i in 1:100){
				result = forward(pixels, w1, w2)
				print(sum(round(result$z3) != labels))
				result = backward(result$z1, result$z2, result$z3, labels, w2)
				print(dim(w1))
				print(dim(result$dw1))
				w1 = w1 - result$dw1
				w2 = w2 - result$dw2
				print(result$dw2)
		}
}

main()
