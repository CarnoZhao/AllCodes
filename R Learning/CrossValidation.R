library(ggplot2)

dataGeneration = function(){
    x1 = rnorm(20, 0, 2)
    x2 = rnorm(20, 0, 2)
    y = ifelse(boundaryFunction(x1) > x2, 1, 0)
    data = data.frame(x1, x2, y)
}

boundaryFunction = function(x){
    x ^ 3 + x ^ 2 - 2 * x - 1
}

splitData = function(ratio, data){
    tr.cv.set = data[1:round(nrow(data) * ratio),]
    test.set = data[round(nrow(data) * ratio) + 1:nrow(data),]
    return(list(tr.cv.set, test.set))
}

crossValidation = function(gamma, tr.cv.set, K){
    for (i in 0:gamma) {
        for (k in 0:(K - 1)){
            tr.set = tr.cv.set[-((1 + nrow(tr.cv.set) * k %/% K):(k + nrow(tr.cv.set) * k %/% K)),]
            cv.set = tr.cv.set[(1 + nrow(tr.cv.set) * k %/% K):(k + nrow(tr.cv.set) * k %/% K),]
            model = learning(tr.set, i)
        }
    }
}

learning = function(tr.set, i){
    X = tr.set$x2
    for (ii in 0:i){
        X = cbind(tr.set$x1 ^ ii, X)
    }
}

data = dataGeneration()
ls = splitData(0.7, data)
tr.cv.set = ls[[1]]
test.set = ls[[2]]
crossValidation(3, tr.cv.set, 1)
