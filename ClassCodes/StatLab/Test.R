library(rethinking)
library(dplyr)
library(ggplot2)
data(Kline)
d = Kline
d$log_pop = log(d$population)
str(d)
graph = ggplot(d, aes(x = log_pop, y = total_tools)) + 
	geom_point() + 
	geom_smooth(method = 'lm', se = FALSE, fullrange = TRUE) + 
	xlim(c(0, 15)) + 
	ylim(c(0, 80))
plot(graph)
model.pois = map(
	alist(
		total_tools ~ dpois(lambda),
		lambda <- exp(a + b * log_pop),
		a ~ dnorm(0, 100),
		b ~ dnorm(0, 1),
		),
	data = d)
model.gaus = map(
	alist(
		total_tools ~ dnorm(mu, sigma),
		mu <- a + b * log_pop,
		a ~ dnorm(-50, 10),
		b ~ dnorm(0, 10),
		sigma ~ dunif(0, 10)),
	data = d)
precis(model.pois, prob = 0.97)
precis(model.gaus, prob = 0.97)