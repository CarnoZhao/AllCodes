x1 = rbinom(1, 2, 0.5)
x2 = rbinom(1, 2, 0.5)
y = rep(1, 2)
d = data.frame(x1, x2, y)
ma = as.matrix(d)
p = ma[sample(1:nrow(d), 2, replace = TRUE),1:2]
l = as.matrix(c(1, 2, 3, 4))
t(l) %*% l
FALSE + FALSE