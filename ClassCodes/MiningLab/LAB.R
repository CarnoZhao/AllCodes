n = 200
x1 = rnorm(n, 0, 3)
x2 = rnorm(n, 0, 3)
# y = as.integer(x1 ^ 2 + x2 ^ 2 < 3)
y = as.integer(x2 > 0 & x1 < 0)
d = data.frame(x1, x2, y)
library(ggplot2)
graph = ggplot(d, aes(x = x1, y = x2, color = as.factor(y))) + geom_point()
w = rep(1 / n, n)
for(j in 1:6){
    minerr = 1
    for(idx in c('x1', 'x2')){
        row = d[,idx]
        for(t in seq(min(row), max(row), 0.5)){
            error = min(mean(w * (d$y != (row > t))), 1 - mean(w * (d$y != (row > t))))
            if(error < minerr){
                minerr = error
                jtlist = list(idx, t)
            }
        }
    }
    alpha = log((1 - minerr) / minerr)
    w = w * exp(alpha * (d$y != (d[,jtlist[[1]]] > jtlist[[2]])))
    w = w / sum(w)
    if(jtlist[[1]] == 'x1'){
        graph = graph + geom_vline(yintercept = jtlist[[2]])
    }
    else{
        graph = graph + geom_hline(yintercept = jtlist[[2]])   
    }
    print(w)
}
plot(graph)