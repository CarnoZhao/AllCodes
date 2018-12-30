rot = function(n){
	i = -1
	while(10 ^ (i + 1) < n){
		i = i + 1
	}
	num1 = n %/% 10 ^ i
	num2 = n %% 10 ^ i
	return(num2 * 10 + num1)
}

maxRot <- function(n) {
  # your code
  
}

rot(123)