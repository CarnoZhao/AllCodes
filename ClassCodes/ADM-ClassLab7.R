k = 2
b = 0
f = function(x1, x2){
	ret = (1 - x1 ^ 2 + x2 ^ 3) * exp(-0.5 * (x1 ^ 2 + x2 ^ 2))
	return(ret)
}

lineRestrict = function(x1){
	x2 = k * x1 + b
	return(x2)
}

f_res = function(x1){
	return(f(x1, lineRestrict(x1)))
}

x1 = seq(-3, 3, length.out = 100)
x2 = seq(-3, 3, length.out = 100)
y = outer(x1, x2, f)

contour(x1, x2, y, xlab = expression(x[1]), ylab = expression(x[2]), 
	main = expression(f(x[1], x[2])), drawlabels = FALSE, nlevels = 10)
abline(a = b, b = k)
curve(f_res, -3, 3)