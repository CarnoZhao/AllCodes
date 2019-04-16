library(rethinking)
d = read.csv('../Data/eagles.csv')
d$pirate_size = ifelse(d$pirate_size == 'large', 1, 0)
d$victim_size = ifelse(d$victim_size == 'large', 1, 0)
model.1 = map2stan(
	alist(
		successes ~ dbinom(size = total_attempts, prob = p),
		logit(p) <- a + bP * pirate_size + bV * victim_size,
		a ~ dnorm(0, 10),
		bP ~ dnorm(0, 5),
		bV ~ dnorm(0, 5)),
	data = d,
	chains = 4)
precis(model.1, 0.97)
