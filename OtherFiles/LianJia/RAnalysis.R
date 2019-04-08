d = read.csv('LianJiaClean.csv')
d = d[complete.cases(d$xaxis),]
library('ggplot2')
library('png')
library('grid')
thres = 10000
d$clear.price = ifelse(d$price > thres, thres, d$price)

map_drawing = function(){
	image = readPNG('Map_2966_2000.png')
	x.lim = c(116.100104, 116.7081914) 
	y.lim = c(39.7689624, 40.078360)
	d = d[d$xaxis < x.lim[2] & d$xaxis > x.lim[1] & d$yaxis < y.lim[2] & d$yaxis > y.lim[1],]
	graph =	ggplot(d, aes(x = xaxis, y = yaxis, color = clear.price)) + 
			annotation_custom(rasterGrob(image, interpolate = T), xmin = x.lim[1], xmax = x.lim[2], ymin = y.lim[1], ymax = y.lim[2]) +
			geom_point() +
			xlim(x.lim) +
			ylim(y.lim) +
			coord_fixed(ratio = 2966 / 2000)
			ggsave('LianJiaRplot.pdf')
}

jitter_drawing = function(){
	bidata.cols = c()
	for (col in colnames(d)){
		if (col == 'price' || col == 'clear.price'){
			next
		}
		if (d[,col] == 1 | d[,col] == 0){
			bidata.cols = c(bidata.cols, col)
		}
	}
	price = d$clear.price
	d = d[,bidata.cols]
	d$price = price
	sapply(
		bidata.cols, 
		function(x){
			graph = ggplot(d, aes(x = d[,x], y = price)) + geom_boxplot() + xlab(x) + ggtitle(paste(c('price~', x), collapse = ''))
			ggsave(paste(c('LianJiaRplot', x, '.pdf'), collapse = ''))
		}
	)
	return()
}

roomspace_price_drawing = function(){
	d$log.price = log10(d$price)
	d = d[d$roomspace < 100,]
	graph = ggplot(d, aes(x = roomspace, y = log.price, color = as.factor(is_subway_house))) + geom_point() + geom_smooth(method = 'lm', formula = y~x)
	ggsave('roomspace_price.pdf')
}

roomspace_price_drawing()
