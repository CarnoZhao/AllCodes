WordsGenerate = function(s){
	letters = strsplit(s, '')[[1]]
	vocabulary = unique(strsplit(paste(letters[which((letters <= 'z' & letters >= 'a') | letters == ' ')], collapse = ''), ' ')[[1]])
	return(vocabulary)
}

LettersMake = function(vocabulary, number, wordlenth){
	lenth = length(vocabulary)
	emailfreq = runif(lenth, 0, 1)
	spamfreq = runif(lenth, 0, 1)
	randomfreq = runif(lenth, 0, 1)
	emailwords = vocabulary[which(emailfreq > randomfreq)]
	spamwords = vocabulary[which(spamfreq > randomfreq)]
	n.email = sample(0:number, 1)
	emails = sapply(rep(0, n.email), function(x){paste(sample(emailwords, replace = TRUE)[1:wordlenth], collapse = ' ')})
	spams = sapply(rep(0, number - n.email), function(x){paste(sample(spamwords, replace = TRUE)[1:wordlenth], collapse = ' ')})
	labels = c(rep(FALSE, n.email), rep(TRUE, number - n.email))
	data = data.frame(c(emails, spams), labels)
	colnames(data) = c('Letters', 'is_Spam')
	data = data[sample(1:nrow(data)),]
	return(data)
}

FreqCalculate = function(vocabulary, data){
	n.email = nrow(filter(data, is_Spam == FALSE))
	n.spam = nrow(filter(data, is_Spam == TRUE))
	email.data = data.frame(strsplit(paste(data[which(data['is_Spam'] == FALSE),1], collapse = ' '), ' ')[[1]])
	spam.data = data.frame(strsplit(paste(data[which(data['is_Spam'] == TRUE),1], collapse = ' '), ' ')[[1]])
	colnames(email.data) = c('words')
	colnames(spam.data) = c('words')
	est.vocabulary = data.frame(sapply(vocabulary, function(x){(nrow(filter(email.data, words == x)) + 1) / (n.email + 1)}), sapply(vocabulary, function(x){(nrow(filter(spam.data, words == x)) + 1) / (n.spam + 1)}), stringsAsFactors = FALSE)
	colnames(est.vocabulary) = c('email.freq', 'spam.freq')
	return(list(est.vocabulary, n.email / n.spam))
}

Estimation = function(newletter, freq.data, email.spam.ratio){
	newwords = strsplit(as.character(newletter), ' ')[[1]]
	p.email = email.spam.ratio / (1 + email.spam.ratio)
	p.spam = 1 / (1 + email.spam.ratio)
	for(word in newwords){
		p.email = p.email * freq.data$email.freq[which(rownames(freq.data) == word)]
		p.spam = p.spam * freq.data$spam.freq[which(rownames(freq.data) == word)]
	}
	return(ifelse(p.email > p.spam, FALSE, TRUE))
}

main = function(number = 1000, wordlenth = 50, training.ratio = 0.7){
	library('dplyr', quietly = TRUE)
	s = 'ab ac ad ae af ag ah ai aj ak al am an ao ap aq ar as at au av aw ax ay az ba bc bd be bf bg bh bi bj bk bl bm bn bo bp bq br bs bt bu bv bw cs ct cu cv cw cx cy cz da db dc de df dg dh di dj dk dl dm dn do dp dq dr ds dt du dv dw dx dy dz ea eb ec ed ef eg eh ei ej ek el em en eo fk fl fm fn fo fp fq fr fs ft fu fv fw fx fy fz ga gb gc gd ge gf gh gi gj gk gl gm gn go gp gq gr gs gt gu gv gw gx gy gz ha hb hc hd he hf ib ic id ie if ig ih ij ik il im in io ip iq ir is it iu iv iw ix iy iz ja jb jc jd je jf jg jh ji jk jl jm jn jo jp jq jr js jt ju jv jw jx kt ku kv kw kx ky kz la lb lc ld le lf lg lh li lj lk lm ln lo lp lq lr ls lt lu lv lw lx ly lz ma mb mc md me mf mg mh mi mj mk ml mn mo mp nk nl nm no np nq nr ns nt nu nv nw nx ny nz oa ob oc od oe of og oh oi oj ok ol om on op oq or os ot ou ov ow ox oy oz pa pb pc pd pe pf pg qc qd qe qf qg qh qi qj qk ql qm qn qo qp qr qs qt qu qv qw qx qy qz ra rb rc rd re rf rg rh ri rj rk rl rm rn ro rp rq rs rt ru rv rw rx ry su sv sw sx sy sz ta tb tc td te tf tg th ti tj tk tl tm tn to tp tq tr ts tu tv tw tx ty tz ua ub uc ud ue uf ug uh ui uj uk ul um un uo up vl vm vn vo vp vq vr vs vt vu vw vx vy vz wa wb wc wd we wf wg wh wi wj wk wl wm wn wo wp wq wr ws wt wu wv wx wy wz xa xb xc xd xe xf xg xh yd ye yf yg yh yi yj yk yl ym yn yo yp yq yr ys yt yu yv yw yx yz za zb zc zd ze zf zg zh zi zj zk zl zm zn zo zp zq zr zs zt zu zv zw zx zy'
	vocabulary = WordsGenerate(s)
	data = LettersMake(vocabulary, number, wordlenth)
	training.set = data[1:as.integer(training.ratio * number),]
	test.set = data[(as.integer(training.ratio * number) + 1):number,]
	result = FreqCalculate(vocabulary, training.set)
	freq.data = result[[1]]
	email.spam.ratio = result[[2]]
	est.labels = sapply(test.set$Letters, function(x){Estimation(x, freq.data, email.spam.ratio)})
	print(length(which(est.labels == test.set$is_Spam)) / (number - as.integer(number * training.ratio)))
}

main()