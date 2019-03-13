image.print <- function(x)
{
x.matrix <- matrix(x, 16, 16, byrow = FALSE)
x.matrix.rotated <- t(apply(x.matrix, 1, rev))
image(x.matrix.rotated, axes = FALSE, col = grey(seq(0, 1, length.out = 256)))
}

pixels = read.table('../data/uspsdata.txt')
labels = as.factor(read.table('../data/uspscl.txt'))
d = data.frame(pixels, labels)
print(class(d[,ncol(d)]))
for(i in 1:4){
	image.print(as.matrix(pixels[i,]))
}
