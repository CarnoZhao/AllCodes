cnt = 21
seq = seq(-10, 10, length.out = cnt)
X = cbind(rep(seq, each = cnt), rep(seq, cnt))
sigmoid = function(x) 1 / (1 + exp(-x))
max0 = function(x) ifelse(x > 0, x, 0)
f = function(X, W, phi){
	Z = phi(X %*% W)
	OUT = Z %*% matrix(rep(1, dim(W)[2]), c(dim(W)[2], 1))
	matrix(OUT, c(cnt, cnt))}

sapply(1:8, function(i){
	ws = rnorm(6, 0, 1)
	par(mfrow = c(1, 3))
	sapply(1:3, function(j){
		fun = ifelse(i < 4, sigmoid, max0)
		persp(x = seq, y = seq, f(X, matrix(ws[1:(2 * j)], c(2, j)), fun),
		xlab = 'x', ylab = 'y', zlab = 'z',
		main = paste(c('#HidenNodes: ', j), collapse = ''),
		theta = 45, phi = 15, col = 'lightblue')

	})	
})
