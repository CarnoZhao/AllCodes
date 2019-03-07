library(rethinking)
d = read.csv('simulated_trees.csv')
centered.height = d$height - mean(d$height)
centered.d = data.frame(centered.height, d$age)
colnames(centered.d) = c('centered.height', 'age')
ggplot(centered.d, aes(x = centered.height, y = d$age)) + 
	geom_point() + 
	xlab('Centered Height') + 
	ylab('Age') + 
	ggtitle('Age ~ Centered Height')
model = map(
	alist(
		age ~ dnorm(mu, sigma), 
		mu <- a + b * height,
		a ~ dnorm(0, 50),
		b ~ dnorm(0, 50),
		sigma ~ dcauchy(0, 5)),
	start = list(a = 50, b = 0, sigma = 50),
	data = d)
precis(model, prob = 0.99)