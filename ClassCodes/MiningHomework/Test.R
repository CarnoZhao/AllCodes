image.print <- function(x)
{
x.matrix <- matrix(x, 16, 16, byrow = FALSE)
x.matrix.rotated <- t(apply(x.matrix, 1, rev))
image(x.matrix.rotated, axes = FALSE, col = grey(seq(0, 1, length.out = 256)))
}

pixels = as.matrix(read.table('../data/uspsdata.txt'))
labels = as.matrix(read.table('../data/uspscl.txt'))
d = data.frame(pixels, as.factor(labels))
head(d)
for(i in 1:4){
	image.print(pixels[i,])
}