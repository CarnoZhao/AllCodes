tankVol <- function(h, d, vt) {
	x = h / d
	floor((acos(1 - 2 * x) - sqrt(x - x ^ 2) * (2 - 4 * x)) * vt / pi)
}

tankVol(5, 7, 3848)