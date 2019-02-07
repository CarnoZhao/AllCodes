n.pos = 75
n.neg = 50
d = 3
set.seed(0)
mu.pos = c(5, 3, 2)
sd.pos = c(1.75, 2, 1)
cor.pos.ij = c(0.2, -0.5, 0.3)
cor.pos = diag(1, d)
cor.pos[lower.tri(cor.pos)] = cor.pos.ij
cor.pos[upper.tri(cor.pos)] = t(cor.pos)[upper.tri(cor.pos)]
Sigma.pos = diag(sd.pos) %*% cor.pos %*% diag(sd.pos)
mu.neg = c(2.5, 1, -2)
sd.neg = c(1.25, 1.5, 1.25)
cor.neg.ij = c(0.3, -0.2, -0.15)
cor.neg = diag(1, d)
cor.neg[lower.tri(cor.neg)] = cor.neg.ij
cor.neg[upper.tri(cor.neg)] = t(cor.neg)[upper.tri(cor.neg)]
Sigma.neg = diag(sd.neg) %*% cor.neg %*% diag(sd.neg)

library(mvtnorm)
x.pos = rmvnorm(n.pos, mu.pos, Sigma.pos)
x.neg = rmvnorm(n.neg, mu.neg, Sigma.neg)

df = data.frame(y = c(rep(1, n.pos), rep(-1, n.neg)), rbind(x.pos, x.neg))

library(rgl)
rgl_init = function(new.device = FALSE, bg = 'white', width = 2000){
	if(new.device || rgl.cur() == 0){
		rgl.open()
		par3d(windowRect = 50 +c(0, 0, width, width))
		rgl.bg(color = bg)
	}
}

rgl_init()
with(df, plot3d(X1, X2, X3, type = 'p', col = ifelse(y == 1, 'red', 'blue'), size = 5, box = FALSE, axes = TRUE))
v.h = c(1, 0, 1)
c = 4
v.h.norm = sqrt(sum(v.h ^ 2))
u.h = v.h / v.h.norm
c = c / v.h.norm
planes3d(u.h[1], u.h[2], u.h[3], d = -c, color = 'gray')

x.1 = c(1, 0, -1)
x.2 = c(0, 0, 0)
lines3d(c(x.1[1], x.2[1]) + c * u.h[1], c(x.1[2], x.2[2]) + c * u.h[2], c(x.1[3], x.2[3]) + c * u.h[3], lwd = 5, color = 'green')
x.1 <- c(1, 5, -1)
x.2 <- c(-1, -5, 1)
lines3d(c(x.1[1], x.2[1]) + c * u.h[1], c(x.1[2], x.2[2]) + c * u.h[2], c(x.1[3], x.2[3]) + c * u.h[3], lwd = 5, color = "green")

i <- 10 # pick a point arbitrarily
x.i <- as.numeric(df[i,c("X1", "X2", "X3")])
alpha <- sum(x.i * u.h)
x.plane <- x.i - alpha * u.h

spheres3d(x.i[1], x.i[2], x.i[3], radius = .2) # adds an orb to highlight the point
lines3d(c(x.i[1], x.plane[1]), c(x.i[2], x.plane[2]), c(x.i[3], x.plane[3]), lwd = 3, col = "gray")