from math import log
import numpy as np

motif = [
"TCGGGGGTTTTT",
"CCGGTGACTTAC",
"ACGGGGATTTTC",
"TTGGGGACTTTT",
"AAGGGGACTTCC",
"TTGGGGACTTCC",
"TCGGGGATTCAT",
"TCGGGGATTCCT",
"TAGGGGAACTAC",
"TCGGGTATAACC"
]

profile = {}
for nt in 'ACGT':
	profile[nt] = [0] * len(motif[0])
for dna in motif:
	for i in range(len(dna)):
		profile[dna[i]][i] += 1
arr = np.array(list(profile.values())) / len(motif)
entropy = 0
for i in range(np.size(arr, 0)):
	for j in range(np.size(arr, 1)):
		if arr[i, j] != 0:
			entropy += - arr[i, j] * log(arr[i, j], 2)
print(entropy)