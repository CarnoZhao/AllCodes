predict_age<-function(age1,age2,age3,age4,age5,age6,age7,age8){
	ages = c(age1, age2, age3, age4, age5, age6, age7, age8)
	return(floor(sqrt(sum(ages ^ 2)) / 2))
}