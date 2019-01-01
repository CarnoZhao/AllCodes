lenth = function(n){
	i = -1
	while(10 ^ (i + 1) < n){i = i + 1}
	return(i)
}

rot = function(n, pos){
	i = lenth(n)
	newn = n %% 10 ^ (i - pos + 1)
	pre = n - newn
	i = i - pos
	num1 = newn %/% 10 ^ i
	num2 = newn %% 10 ^ i
	return(pre + num2 * 10 + num1)
}

maxRot <- function(n) {
	i = 0
	list = c(n)
	while(i < lenth(n)){
		n = rot(n, i)
		list = c(list, n)
		i = i + 1
	}
	return(list)
}

maxRot(240522578)