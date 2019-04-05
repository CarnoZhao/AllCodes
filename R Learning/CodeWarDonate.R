newAvg <- function(arr, newavg){
	n = newavg * (length(arr) + 1) - sum(arr)
	return(ifelse(n > 0, n, ValueError))
}

newAvg(c(14, 30, 5, 7, 9, 11, 15), 2)