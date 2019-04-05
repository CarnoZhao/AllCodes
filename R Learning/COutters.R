clean_mean <- function(sam, cutoff){
	len = length(sam)
	avg = mean(sam)
	vars = sd(sam) * sqrt((len - 1) / len)
	newsam = sam[which(sam < cutoff * vars + avg & sam > avg - cutoff * vars)]
	if(length(newsam) == len){
		return(round(avg, 1))
	} else{
		return(clean_mean(newsam, cutoff))
	}
}

sam = c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100)
cutoff = 3
clean_mean(sam, cutoff)