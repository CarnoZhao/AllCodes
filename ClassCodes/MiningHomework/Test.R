train_g = function(m, data){
    x.pos.s = as.matrix(data[data[ncol(data)] == 1, -ncol(data)])
    x.neg.s = as.matrix(data[data[ncol(data)] != 1, -ncol(data)])
    pos.index = sample(1:nrow(x.pos.s), m, replace = TRUE)
    neg.index = sample(1:nrow(x.neg.s), m, replace = TRUE)
    x.pos.m = x.pos.s[pos.index,]
    x.neg.m = x.neg.s[neg.index,]
    if(m == 1){
        x.pos.m = t(as.matrix(x.pos.m))
        x.neg.m = t(as.matrix(x.neg.m))
    }
    w.m = (x.pos.m - x.neg.m) / rowSums((x.pos.m - x.neg.m) ^ 2)
    c.w.m = rowSums(w.m * (x.pos.m + x.neg.m) / 2)
    misc = 
        rowSums(w.m %*% t(x.pos.s) < c.w.m) + 
        rowSums(w.m %*% t(x.neg.s) > c.w.m)
    v = w.m * ifelse(misc > nrow(data) / 2, -1, 1)
    c = rowSums(v * (x.pos.m + x.neg.m) / 2)
    return(list(v, c))
}

classify = function(x, V, c){
    return(sign(colSums(sign(V %*% t(x) - c))))
}

hw = function(){
    data.d = read.csv('../Data/wdbc.data')
    data.l = read.csv('../Data/wdbc.labels')
    data = data.frame(data.d, data.l)
    data = data[sample(1:nrow(data)),]
    data.tr = data[1:round(nrow(data) / 2),]
    data.ts = data[(round(nrow(data) / 2) + 1):nrow(data),]
    m.seq = seq(1, 199, 2)
    err.rates = sapply(
        m.seq, 
        function(m){
            Vc = train_g(m, data.tr)
            V = Vc[[1]]
            c = Vc[[2]]
            esti = classify(data.ts[,-ncol(data.ts)], V, c)
            err.rate = mean(esti != data.ts[,ncol(data.ts)])
            return(err.rate)
        }
    )
    library(ggplot2)
    graph = ggplot(data.frame(cbind(m.seq, err.rates)), 
        aes(x = m.seq, y = err.rates)) + 
        geom_smooth(formula = y ~ x, method = 'loess') +
        geom_point() +
        xlab('m') +
        ylab('Error Rate')
    plot(graph)
}

easyPlot = function(){
    x1 = c(rnorm(100, 0, 1), rnorm(100, 2, 1))
    x2 = c(rnorm(100, 0, 1), rnorm(100, 2, 1))
    x3 = c(rnorm(100, 0, 1), rnorm(100, 2, 1))
    x4 = c(rnorm(100, 0, 1), rnorm(100, 2, 1))
    y = c(rep(1, 100), rep(-1, 100))
    data = data.frame(x1, x2, x3, x4, y)
    Vc = train_g(100, data)
    V = Vc[[1]]
    c = Vc[[2]]
    esti = classify(data[,-ncol(data)], V, c)
    newdata = cbind(data, esti)
    library(ggplot2)
    shape = c(20, 4)
    names(shape) = c('TRUE', 'FALSE')
    graph = ggplot(data, aes(x = x1, y = x2, color = as.factor(esti), shape = as.factor(y == esti))) +
        geom_point() + 
        scale_shape_manual(values = shape)
    print(mean(y != esti))
    plot(graph)
}

hw()