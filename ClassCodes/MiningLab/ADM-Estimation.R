prepareData = function(n){
  means = runif(2, 0, 1)
  vars = runif(4, 0.5, 1)
  
  x11 = rnorm(n, means[1], vars[1])
  x12 = rnorm(n, means[2], vars[2])
  x21 = rnorm(n, means[1] + 1, vars[3])
  x22 = rnorm(n, means[2] + 1, vars[4])
  
  x1 = c(x11, x21)
  x2 = c(x12, x22)
  y = c(rep(1, n), rep(-1, n))
  
  d = data.frame(y, x1, x2)
  #graph = ggplot(data, mapping = aes(y = x2, x = x1, color = as.factor(y)))
  #plot(graph + geom_point())
  return(d)
}

estimation = function(data, newx){
  newx = matrix(newx)
  x1 = t(data.matrix(data[,(2:3)][which(data[,1] == 1),]))
  x2 = t(data.matrix(data[,(2:3)][which(data[,1] == -1),]))
  mu1 = rowMeans(x1)
  mu2 = rowMeans(x2)
  cov1 = ((x1 - mu1) %*% t(x1 - mu1)) / length(x1)
  cov2 = ((x2 - mu2) %*% t(x2 - mu2)) / length(x2)
  p1 = exp(-0.5 * t(newx - mu1) %*% solve(cov1) %*% (newx - mu1)) / sqrt((2 * pi) ^ length(newx) * det(cov1))
  p2 = exp(-0.5 * t(newx - mu2) %*% solve(cov2) %*% (newx - mu2)) / sqrt((2 * pi) ^ length(newx) * det(cov2))
  return(ifelse(p1 > p2, 1, -1))
}

main = function(n){
  library(ggplot2)
  data = prepareData(n)
  xs = data.matrix(data[,(2:3)])
  ys = data.matrix(data[1])
  ans = apply(xs, 1, function(x){estimation(data, x)}) == ys
  lossdata = data.frame(ans, xs)
  graph = ggplot(lossdata, mapping = aes(y = xs[,2], x = xs[,1], color = ans))
  plot(graph + geom_point())
  print(1 - sum(ans) / (2 * n))
}

main(100)