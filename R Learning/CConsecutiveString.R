longestConsec <- function (strarr, k) {
	if(length(strarr) == 0 || k <= 0 || k > length(strarr)){
		return('')
	}
	maxcnt = 0
	maxi = 1
	for(i in 1:(length(strarr) - k + 1)){
		if(i == 1){
			cnt = sum(unlist(lapply(strarr[i:(i + k - 1)], nchar)))
		} else{
			cnt = cnt + nchar(strarr[i + k - 1]) - nchar(strarr[i - 1])
		}
		if(cnt > maxcnt){
			maxcnt = cnt
			maxi = i
		}
	}
	return(paste(strarr[maxi:(maxi + k - 1)], collapse = ''))
}

longestConsec(c("zone", "abigail", "theta", "form", "libe", "zas"), 2)