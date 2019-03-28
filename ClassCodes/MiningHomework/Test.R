train_g = function(m, data){
    vectors = data[-ncol(data)]
    labels = ifelse(data[,ncol(data)] == data[1,ncol(data)], 1, -1)
    pairs = sapply(1:m, function(i){
        x.pos = vectors[sample(row.names(vectors[labels == 1,]), 1),]
        x.neg = vectors[sample(row.names(vectors[labels == -1,]), 1),]
        w = (x.pos - x.neg) / sum((x.pos - x.neg) ^ 2)
        c.w = sum(w * (x.pos + x.neg) / 2)
        misc = sum(sign(as.matrix(w) %*% t(as.matrix(vectors)) - c.w) != labels)
        s = ifelse(misc < nrow(data) / 2, 1, -1)
        v = s * w
        c = sum(v * (x.pos + x.neg) / 2)
        return(c(as.matrix(v), c))
    })
    return(list(t(pairs[1:ncol(vectors),]), as.matrix(pairs[nrow(pairs),])))
}

classify = function(x, V, c){
    return(sign(sum(sign(V %*% as.matrix(x) - c))))
}

easyPlot = function(){
    x1 = c(rnorm(100, 0, 1), rnorm(100, 2, 1))
    x2 = c(rnorm(100, 0, 1), rnorm(100, 2, 1))
    x3 = c(rnorm(100, 0, 1), rnorm(100, 2, 1))
    x4 = c(rnorm(100, 0, 1), rnorm(100, 2, 1))
    x5 = c(rnorm(100, 0, 1), rnorm(100, 2, 1))
    x6 = c(rnorm(100, 0, 1), rnorm(100, 2, 1))
    x7 = c(rnorm(100, 0, 1), rnorm(100, 2, 1))
    y = c(rep(1, 100), rep(-1, 100))
    data = data.frame(x1, x2, y)
    Vc = train_g(1, data)
    V = Vc[[1]]
    c = Vc[[2]]
    esti = apply(t(as.matrix(data[,-ncol(data)])), 2, classify, V = V, c = c)
    newdata = cbind(data, esti)
    library(ggplot2)
    shape = c(20, 4)
    names(shape) = c('TRUE', 'FALSE')
    graph = ggplot(data, aes(x = x1, y = x2, color = as.factor(esti), shape = as.factor(y == esti))) +
        geom_point() + 
        scale_shape_manual(values = shape)
    print(sum(y != esti) / length(y))
    plot(graph)
}

hw = function(){
    data.d = read.csv('../Data/wdbc.data')
    data.l = read.csv('../Data/wdbc.labels')
    data = data.frame(data.d, data.l)
    data = data[sample(1:nrow(data)),]
    data.tr = data[1:round(nrow(data) / 2),]
    data.ts = data[(round(nrow(data) / 2) + 1):nrow(data),]

    m.seq = seq(1, 59, 2)
    err.rates = sapply(
        m.seq, 
        function(m){
            Vc = train_g(m, data.tr)
            V = Vc[[1]]
            c = Vc[[2]]
            esti = apply(
                t(as.matrix(data.ts[,-ncol(data.ts)])), 2, 
                classify, V = V, c = c
                )
            err.rate = sum(esti != data.ts[,ncol(data.ts)]) / nrow(data.ts)
            return(err.rate)
            }
        )
    library(ggplot2)
    graph = ggplot(
        data.frame(cbind(m.seq, err.rates)), 
        aes(x = m.seq, y = err.rates)
        ) + 
        geom_point()
    plot(graph)
}

easyPlot()