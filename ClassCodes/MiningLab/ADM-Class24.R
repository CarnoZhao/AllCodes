setwd('D:/Codes/ClassCodes/MiningLab/')
# pixels = as.matrix(read.table('../Data/uspsdata.txt'))
# labels = as.matrix(read.table('../Data/uspscl.txt'))
# labels = ifelse(labels == 1, 1, 0)
mnist_raw <- read_csv("https://pjreddie.com/media/files/mnist_train.csv", col_names = FALSE)

m = 200
n1 = 256
n2 = 100
n3 = 1

sigmoid = function(x){
		1 / (1 + exp(-x))
}

weight = function(){
		w1 = runif((n1 + 1) * n2, -4, 4)
		dim(w1) = c(n1 + 1, n2)
		w2 = runif((n2 + 1) * n3, -1, 1)
		dim(w2) = c(n2 + 1, n3)
		return(list(w1 = w1, w2 = w2))
}

forward = function(pixels, w1, w2){
		z1 = cbind(m, pixels)
		z2 = cbind(m, sigmoid(z1 %*% w1))
		z3 = sigmoid(z2 %*% w2)
		return(list(z1 = z1, z2 = z2, z3 = z3))
}

backward = function(z1, z2, z3, labels, w2){
		dw2 = t(z2) %*% (labels - z3)
		dw1 = t(z1) %*% (((labels - z3) %*% t(w2)) * z2 * (1 - z2))[,-1]
		return(list(dw1 = dw1 / m, dw2 = dw2 / m))
}

main = function(){
		w1_w2 = weight()
		w1 = w1_w2$w1
		w2 = w1_w2$w2
		right = 0
		i = 0
		while (right < 0.999){
				result1 = forward(pixels, w1, w2)
				right = mean(round(result1$z3) == labels)
				result2 = backward(result1$z1, result1$z2, 
				                   result1$z3, labels, w2)
				w1 = w1 + result2$dw1
				w2 = w2 + result2$dw2
				i = i + 1
		}
		print("Error Rate:")
		print(1 - right)
		print("Steps:")
		print(i)
}

main()
