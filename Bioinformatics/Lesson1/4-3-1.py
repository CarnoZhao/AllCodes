def file_name(path):
	import os
	filelist = os.listdir(path)
	timelist = list(map(lambda x: os.stat(path + x).st_mtime, filelist))
	return path + filelist[timelist.index(max(timelist))]

def load_file(filename):
	f = open(filename)
	k, t, N = tuple(map(lambda x: eval(x), f.readline().rstrip().split(' ')))
	dnas = [l.rstrip() for l in f]
	f.close()
	return k, t, N, dnas

def profile_make(motif, k):
	import numpy as np
	profile = np.zeros((4, k))
	for dna in motif:
		for j, nt in enumerate(dna):
			i = 'ACGT'.index(nt)
			profile[i][j] += 1
	score = 0
	for j in range(np.size(profile, 1)):
		maxcnt = 0
		for i in range(4):
			if profile[i][j] > maxcnt:
				score += maxcnt
				maxcnt = profile[i][j]
			else:
				score += profile[i][j]
	profile = (profile + np.ones(np.shape(profile))) / (len(motif) + 4)
	return score, profile.tolist()

def find_kmer(dna, profile, k):
	ret = dna[:k]
	maxpr = 0
	for i in range(len(dna) - k + 1):
		kmer = dna[i: i + k]
		pr = 1
		for j, nt in enumerate(kmer):
			i = 'ACGT'.index(nt)
			pr *= profile[i][j]
		if pr > maxpr:
			maxpr = pr
			ret = kmer
	return ret

def main():
	import random
	path = 'D:/Browser Download/'
	filename = file_name(path)
	k, t, N, dnas = load_file(filename)
	iter_time = 20
	retscore = 10000
	for time in range(iter_time):
		bestmotif = []
		for dna in dnas:
			i = random.randint(0, len(dna) - k)
			bestmotif.append(dna[i: i + k])
		bestscore, bestprofile = profile_make(bestmotif, k)
		for gibbs_time in range(N):
			motif = bestmotif
			exclude_i = random.randint(0, t - 1)
			motif[exclude_i] = ''
			score, profile = profile_make(motif, k)
			motif[exclude_i] = find_kmer(dnas[exclude_i], profile, k)
			score, profile = profile_make(motif, k)
			if score < bestscore:
				bestscore, bestprofile, bestmotif = score, profile, motif
		if bestscore < retscore:
			ret, retscore = bestmotif, bestscore
	print('\n'.join(ret))
	print(retscore)

main()