fitFunc = function(x){
	return(sqrt(sum(c(1:x)[which(x %% c(1:x) == 0)] ^ 2))) ^ 2 == sum(c(1:x)[which(x %% c(1:x) == 0)])))
}

listSquared <- function (m, n) {
	0
}

fitFunc(42)