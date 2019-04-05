PLOT = function(){
    dis = c(266.068,292,326,376.021,468,502.004,870.009)
    bps = c(23130,9416,6557,4361,2322,2027,564)
    log.bps = log10(bps)
    print(log.bps)
    re.log = 1/log.bps
    d = data.frame(dis, bps, log.bps, re.log)
    library(ggplot2)
    rawd = d
    #d = d[-nrow(d),]
    lm_eqn <- function(df){
        m <- lm(log.bps ~ dis, df);
        eq <- substitute(italic(log(n)) == a + (b) %.% italic(d)*","~~italic(r)^2~"="~r2, 
             list(a = format(coef(m)[[1]], digits = 6), 
                  b = format(coef(m)[[2]], digits = 6), 
                 r2 = format(summary(m)$r.squared, digits = 3)))
        as.character(as.expression(eq));                 
    }

    lm_eqn2 <- function(df){
        m <- lm(re.log ~ dis, df);
        eq <- substitute(italic(log(n)) == a + b %.% italic(d)*","~~italic(r)^2~"="~r2, 
             list(a = format(coef(m)[[1]], digits = 6), 
                  b = format(coef(m)[[2]], digits = 6), 
                 r2 = format(summary(m)$r.squared, digits = 3)))
        as.character(as.expression(eq));                 
    }


    graph = ggplot(d, aes(x = dis, y = log.bps)) + 
        geom_point() +
        xlab('d') + 
        ylab('ln(n)') + 
        ggtitle('log(n) ~ d')
    ggsave('raw_point.png', plot = graph)
    for (i in 1: 4){
        newd = d[i:nrow(d),]
        graph = ggplot(newd, aes(x = dis, y = log.bps)) +     geom_point() +
            xlab('d') + 
            ylab('log(n)') + 
            ggtitle('log(n) ~ d') + 
            geom_smooth(method = 'lm', se = FALSE) + 
            geom_text(x = quantile(newd$dis, 0.7), y = quantile(newd$log.bps, 0.1), label = lm_eqn(newd), parse = TRUE)
        plot(graph)
        ggsave(paste(c('discard_', as.character(i), '.png'), collapse = ''), plot = graph)
        #model = lm(log.bps ~ dis, data = d[i:nrow(d),])
        #print(summary(model))
    }
    i = 4
    model = lm(log.bps ~ dis, data = d[i:nrow(d),])
    a = coef(model)[[1]]
    b = coef(model)[[2]]
    graph = ggplot(rawd, aes(x = dis, y = log.bps)) + 
        geom_point() +
        xlab('d') + 
        ylab('ln(n)') + 
        ggtitle('log(n) ~ d')
    newgraph = graph + geom_abline(intercept = a, slope = b)
    plot(newgraph)
    ggsave('raw_points_line.png', plot = newgraph)
    for (i in 1: 4){
        newd = d[i:nrow(d),]
        graph = ggplot(newd, aes(x = dis, y = re.log)) + 
            geom_point() +
            xlab('d') + 
            ylab('log(n)') + 
            ggtitle('log(n) ~ d') + 
            geom_smooth(method = 'lm', se = FALSE) + 
            geom_text(x = mean(newd$dis), y = mean(newd$re.log), label = lm_eqn2(newd), parse = TRUE)
        plot(graph)
    }
}

error = function(x){
    x_1 = x[1]
    x_2 = x[2]
    x_3 = x[3]
    x_4 = 1 - sum(x)
    (x_1 + x_2 - 0.738) ^ 2 + (x_1 + x_2 - 0.743) ^ 2 + (x_3 + x_4 - 0.262) ^ 2 + (x_3 + x_4 - 0.27) ^ 2 + (x_3 + x_4 - 0.243) ^ 2 + (x_1 - 0.434)^2 + (x_1 - 0.44)^2 + (x_2 - 0.323)^2 + (x_2 - 0.332)^2 + (x_3 - 0.152)^2 + (x_3 - 0.136)^2 + (x_4 - 0.105)^2 + (x_4 - 0.092)^2 + (0.514 - x_1 - x_4) ^2 + (0.486 - x_2 - x_3)^ 2
}

OPTIM = function(){
    optim(par = c(0.25, 0.25, 0.25), error)
}

x = OPTIM()
par = c(x$par, 1 - sum(x$par))
y = sapply(par, function(x){round(x, 3)})
y
sum(y)