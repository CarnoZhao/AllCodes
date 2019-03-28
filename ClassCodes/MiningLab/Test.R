x1 = rnorm(100, 0, 1)
x2 = rnorm(100, 0, 1)
y = rep(1, 100)
d = data.frame(x1, x2, y)
ma = as.matrix(d)
p = ma[sample(1:nrow(d), 5, replace = TRUE),1:2]
p

p * c(10, 20, 1, 0, 0)