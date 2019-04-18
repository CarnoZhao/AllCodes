
library(rethinking)
d.2 = data.frame(infect = c(rep(1, 9), rep(0, 11)))
model.3 = map2stan(
				   alist(
						 infect ~ dbinom(1, p),
						 logit(p) <- a,
						 a ~ dunif(-Inf, 0)),
				   start = list(a = -5),
				   data = d.2,
				   chains = 4)
precis(model.3, 0.97)
sample.3 = extract.sample(model.3, 10000)
dens(sample.3$a)
print(logistic(mean(sample.3$a)))