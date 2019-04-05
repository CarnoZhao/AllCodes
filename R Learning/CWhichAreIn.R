inArray <- function(a1, a2) {
	print(a1)
	print(a2)
	check = unlist(lapply(a1, function(x){sum(unlist(lapply(a2, function(y){grepl(x, y)})))}))
	ret = sort(a1[which(check > 0)])
	if(length(ret) == 0){
		return(NULL)
	} else{
		return(ret[!duplicated(ret)])
	}
}

a1 = c("livea", "arpa", "stronga") 
a2 = c("lively", "alive", "harp", "sharp", "armstrong")
inArray(a1, a2)