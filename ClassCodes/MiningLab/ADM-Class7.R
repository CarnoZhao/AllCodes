f = function(x1, x2){
	ret = (1 - x1 ^ 2 + x2 ^ 3) * exp(-0.5 * (x1 ^ 2 + x2 ^ 2))
	return(ret)
}

lineRestrict = function(x1){
	x2 = k * x1 + b
	return(x2)
}

x1 = seq(-3, 3, length.out = 100)
x2 = seq(-3, 3, length.out = 100)
y = outer(x1, x2, f)

contour(x1, x2, y, xlab = expression(x[1]), ylab = expression(x[2]), 
	main = expression(f(x[1], x[2])), drawlabels = FALSE, nlevels = 10)
x2.0 = 0.5
abline(h = x2.0)
fr = function(x1) {f(x1, x2.0)}
curve(fr, -3, 3, main = 'Horizontal Slice')

g = function(x1, x2){
	c(
		-x1 * (3 - x1 ^ 2 + x2 ^ 3) * exp(-0.5 * (x1 ^ 2 + x2 ^ 2)),
		-x2 * (1 - x1 ^ 2 - 3 * x2 + x2 ^ 3) * exp(-0.5 * (x1 ^ 2 + x2 ^ 2))
	)
}
gr = function(x1) {
	g(x1, x2.0)[1]
}

x1.0 = 0.15
m = gr(x1.0)
b = fr(x1.0) - x1.0 * m
abline(b, m)
points(x1.0, fr(x1.0), pch = 16)

x1.0 = 1.6
m = gr(x1.0)
b = fr(x1.0) - x1.0 * m
abline(b, m)
points(x1.0, fr(x1.0), pch = 16)

x.0 = runif(2, -3, 3)
v = rnorm(2)
v = v / sqrt(sum(v ^ 2))