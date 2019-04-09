library(rethinking)
library(dplyr)
library(ggplot2)
data(Kline)
d = Kline
d$log_pop = log(d$population)
str(d)
model.pois = map(
	alist(
		total_tools ~ dpois(lambda),
		lambda <- exp(a + b * log_pop),
		a ~ dnorm(0, 100),
		b ~ dnorm(0, 1)
		),
	data = d)
