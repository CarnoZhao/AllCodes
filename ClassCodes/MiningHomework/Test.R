image.print <- function(x)
{
x.matrix <- matrix(x, 16, 16, byrow = FALSE)
x.matrix.rotated <- t(apply(x.matrix, 1, rev))
image(x.matrix.rotated, axes = FALSE, col = grey(seq(0, 1, length.out = 256)))
}

pixels = as.matrix(read.table('../data/uspsdata.txt'))
labels = as.matrix(read.table('../data/uspscl.txt'))
nums = nrow(pixels)
for(i in 1:4){
	image.print(pixels[i,])
}
p.tr = pixels[1:round(nums * 0.6),]
l.tr = labels[1:round(nums * 0.6),]
p.cv = pixels[(round(nums * 0.6) + 1):round(nums * 0.8),]
l.cv = labels[(round(nums * 0.6) + 1):round(nums * 0.8),]
p.ts = pixels[(round(nums * 0.8) + 1):nums,]
l.ts = labels[(round(nums * 0.8) + 1):nums,]

library(class)
estim = knn(p.tr, p.ts, cl = l.tr, k = 1)
err.rate = sum(estim != l.ts) / length(estim)
print(err.rate)

rows = which(estim != l.ts) + round(nums * 0.6)
for (row in rows){
	image.print(pixels[row,])
}

k.seq = seq(1, 13, 2)
error.rates = sapply(
	k.seq, 
	function(k){
		estim = knn(p.tr, p.ts, cl = l.tr, k = k)
		sum(estim != l.ts) / length(estim)
})
print(rbind(k.seq, error.rates))

k.optim = k.seq[which(error.rates == min(error.rates))]
print(k.optim)
estim = knn(rbind(p.tr, p.ts), p.cv, cl = c(l.tr, l.ts), k = k.optim)
error.rate = sum(estim != l.cv) / length(estim)
print(error.rate)