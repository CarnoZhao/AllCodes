def file_name(path):
	import os
	filelist = os.listdir(path)
	timelist = list(map(lambda x: os.stat(path + x).st_mtime, filelist))
	filename = filelist[timelist.index(max(timelist))]
	return path + filename

def load_file(filename):
	f = open(filename)
	k, t = tuple(map(lambda x: eval(x), f.readline().rstrip().split(' ')))
	dnas = []
	for l in f:
		dnas.append(l.rstrip())
	f.close()
	return k, t, dnas

def profile_make(motif):
	import numpy as np
	profile = np.zeros((4, len(motif[0])))
	for dna in motif:
		for j, nt in enumerate(dna):
			i = 'ACGT'.index(nt)
			profile[i][j] += 1
	score = 0
	for j in range(np.size(profile, 1)):
		maxcnt = 0
		for i in range(np.size(profile, 0)):
			if profile[i][j] > maxcnt:
				score += maxcnt
				maxcnt = profile[i][j]
			else:
				score += profile[i][j]
	profile = (profile + np.ones(np.shape(profile))) / (len(motif) + 4)
	return score, profile.tolist()

def find_kmer(profile, dna, k):
	maxpr = 0
	ret = dna[:k]
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

def find_motif():
	import random
	path = 'D:/Browser Download/'
	filename = file_name(path)
	k, t, dnas = load_file(filename)
	iter_time = 1000
	retscore = 1000
	for time in range(iter_time):
		bestmotif = []
		for dna in dnas:
			i = random.randint(0, len(dna) - k)
			bestmotif.append(dna[i: i + k])
		bestscore, bestprofile = profile_make(bestmotif)
		while True:
			motif = []
			for dna in dnas:
				motif.append(find_kmer(bestprofile, dna, k))
			score, profile = profile_make(motif)
			if score < bestscore:
				bestscore, bestmotif, bestprofile = score, motif, profile
			else:
				break
		if bestscore < retscore:
			ret = bestmotif
			retscore = bestscore
	return '\n'.join(ret)

print(find_motif())