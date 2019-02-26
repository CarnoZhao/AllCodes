n = 200 # sample size
d = 2 # features
x = matrix(runif(n * d, -10, 10), nrow = n)
v = runif(d, -1, 1)
c = runif(1)
prob = plogis(x %*% v - c)
y = rbinom(n, 1, prob = prob)
library(ggplot2)
d = data.frame(x, y)
X1 = d$X1
X2 = d$X2
ggplot(d, aes(x = X1, y = X2, color = as.factor(y))) + geom_point()
mf = model.frame(y ~ -1 + X1 + X2, d)
data = list(x = model.matrix(mf), y = model.response(mf))
print(data[1])
print('#######')
print(data[2])