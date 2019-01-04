fitFunc = function(x){
	sqdivs = sqrt(sum(c(1:x)[which(x %% c(1:x) == 0)] ^ 2))
	check = sqdivs == floor(sqdivs)
	return(check)
}

listSquared <- function (m, n) {
	allfits = c(m:n)[which(sapply(c(m:n), fitFunc))]
	return(lapply(allfits, function(x){c(x, sum(c(1:x)[which(x %% c(1:x) == 0)] ^ 2))}))
}

listSquared(40, 250)