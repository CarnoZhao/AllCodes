accum <- function(s){
	# Your code
	s = strsplit(tolower(s), '')[[1]]
	string = ''
	for (i in 1:length(s)){
		string = paste(string, ifelse(i == 1, '', '-'), toupper(s[i]), paste(rep(s[i], i - 1), collapse = ''), sep = '')
	}
	return(string)
}

accum('abcd')