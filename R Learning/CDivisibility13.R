thirt <- function (n) {
	vec = c(1, 10, 9, 12, 3, 4)
	nextn = -1
	while(nextn != n){
		n = ifelse(nextn == -1, n, nextn)
		divn = rev(unlist(lapply(unlist(strsplit(as.character(n), '')), as.numeric)))
		nextn = sum(divn * vec[1:min(c(length(divn), length(vec)))])
	}
	return(nextn)
}

thirt(1234567)