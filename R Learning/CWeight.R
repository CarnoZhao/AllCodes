st = "10003 1234000 44444444 9999 2000 123456789"

changenewweight = function(string){
	return(sum(unlist(lapply(strsplit(string, ''), as.numeric))))
}

orderWeight <- function(st) {
	weights = strsplit(st, ' ')[[1]]
	weights = weights[which(weights != '')]
	newweights = sort(unlist(lapply(weights, changenewweight)))
	vec = c()
	for(neww in newweights[!duplicated(newweights)]){
		vec = c(vec, sort(weights[which(unlist(lapply(weights, changenewweight)) == neww)]))
	}
	return(paste(vec, collapse = ' '))
}

orderWeight(st)