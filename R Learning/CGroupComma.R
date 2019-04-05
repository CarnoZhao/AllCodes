group_by_commas <- function(n){
	string = rev(unlist(strsplit(as.character(as.integer(n)), '')))
	i = 1
	vec = c()
	while(i <= length(string)){
		vec = c(vec, string[i])
		if(i %% 3 == 0 && i != length(string)){
			vec = c(vec, ',')
		}
		i = i + 1
	}
	return(paste(rev(vec), collapse = ''))
}

group_by_commas(297651925)