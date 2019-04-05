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
	return k, t, dnas

def profile_make(motif):
	import numpy as np
	profile = np.zeros((4, len(motif[0])))
	for dna in motif:
		for j, nt in enumerate(dna):
			i = 'ACGT'.index(nt)
			profile[i][j] += 1
	score = 0
	for j in range(len(profile[0])):
		maxcnt = 0
		for i in range(len(profile)):
			if profile[i][j] > maxcnt:
				score += maxcnt
				maxcnt = profile[i][j]
			else:
				score += profile[i][j]
	profile = ((profile + np.ones(np.shape(profile)))/ (len(motif) + 4)).tolist()
	return profile, score

def find_kmer(profile, k, dna):
	maxpr = 0
	ret = dna[:k]
	for i in range(len(dna) - k + 1):
		part = dna[i: i + k]
		pr = 1
		for l, nt in enumerate(part):
			j = 'ACGT'.index(nt)
			pr *= profile[j][l]
		if pr > maxpr:
			maxpr = pr
			ret = part
	return ret

def main():
	path = 'D:/Browser Download/'
	filename = file_name(path)
	k, t, dnas = load_file(filename)
	bestmotif = []
	for i in range(t):
		bestmotif.append(dnas[i][:k])
	profile, bestscore = profile_make(bestmotif)
	for i in range(len(dnas[0]) - k + 1):
		motif = [dnas[0][i: i + k]]
		profile, score = profile_make(motif)
		for dna in dnas[1:]:
			kmer = find_kmer(profile, k, dna)
			motif.append(kmer)
			profile, score = profile_make(motif)
		if score < bestscore:
			bestscore = score
			bestmotif = motif
	print('\n'.join(bestmotif))
	print(bestscore)

main()