from LoadFile import LoadFile
from collections import defaultdict

def Score(protein, e_spec):
	prefix = [0]
	for aa in protein:
		prefix.append(aa + prefix[-1])
	t_spec = [0]
	for i in range(len(prefix)):
		for j in range(i + 1, len(prefix)):
			t_spec.append(prefix[j] - prefix[i])
			#if i != 0 and j != len(prefix) - 1:#for cycle peptide
			#	t_spec.append(prefix[-1] - prefix[j] + prefix[i])
	ret = 0
	for pep in set(t_spec):
		ret += min(t_spec.count(pep), e_spec.count(pep))
	return ret

f = open(LoadFile())
N = eval(f.readline().rstrip())
e_spec = list(map(lambda x: eval(x), f.readline().rstrip().split(' ')))
f.close()
#Example
#e_spec = list(map(lambda x: eval(x), '0 71 71 71 87 97 97 99 101 103 113 113 114 115 128 128 129 137 147 163 163 170 184 184 186 186 190 211 215 226 226 229 231 238 241 244 246 257 257 276 277 278 299 300 312 316 317 318 318 323 328 340 343 344 347 349 356 366 370 373 374 391 401 414 414 415 419 427 427 431 437 441 446 453 462 462 462 470 472 502 503 503 511 515 529 530 533 533 540 543 547 556 559 569 574 575 584 590 600 600 604 612 616 617 630 640 640 643 646 648 660 671 683 684 687 693 703 703 719 719 719 729 730 731 737 740 741 745 747 754 774 780 784 790 797 800 806 818 826 827 832 833 838 846 846 847 850 868 869 877 884 889 893 897 903 908 913 917 930 940 947 956 960 960 961 964 965 966 983 983 985 1002 1009 1010 1011 1021 1031 1031 1036 1053 1054 1058 1059 1062 1063 1074 1076 1084 1092 1103 1113 1122 1124 1130 1133 1134 1145 1146 1146 1149 1150 1155 1156 1171 1173 1174 1187 1191 1193 1200 1212 1221 1233 1240 1242 1246 1259 1260 1262 1277 1278 1283 1284 1287 1287 1288 1299 1300 1303 1309 1311 1320 1330 1341 1349 1357 1359 1370 1371 1374 1375 1379 1380 1397 1402 1402 1412 1422 1423 1424 1431 1448 1450 1450 1467 1468 1469 1472 1473 1473 1477 1486 1493 1503 1516 1520 1525 1530 1536 1540 1544 1549 1556 1564 1565 1583 1586 1587 1587 1595 1600 1601 1606 1607 1615 1627 1633 1636 1643 1649 1653 1659 1679 1686 1688 1692 1693 1696 1702 1703 1704 1714 1714 1714 1730 1730 1740 1746 1749 1750 1762 1773 1785 1787 1790 1793 1793 1803 1816 1817 1821 1829 1833 1833 1843 1849 1858 1859 1864 1877 1886 1890 1893 1900 1900 1903 1904 1918 1922 1930 1930 1931 1961 1963 1971 1971 1971 1980 1987 1992 1996 2002 2006 2006 2014 2018 2019 2019 2032 2042 2059 2060 2063 2067 2077 2084 2086 2089 2090 2093 2105 2110 2115 2115 2116 2117 2121 2133 2134 2155 2156 2157 2176 2176 2187 2189 2192 2195 2202 2204 2207 2207 2218 2222 2243 2247 2247 2249 2249 2263 2270 2270 2286 2296 2304 2305 2305 2318 2319 2320 2320 2330 2332 2334 2336 2336 2346 2362 2362 2362 2433'.split(' ')))

masstable = []
f = open('integer_mass_table.txt')
for l in f:
	masstable.append(eval(l.rstrip().split(' ')[1]))
f.close()

peps = [[]]
cnt = 0
maxe = max(e_spec)
maxt = 0
while maxt < maxe:
	scorelist = []
	temp = []
	for pep in peps:
		for aa in masstable:
			scorelist.append([Score(pep + [aa], e_spec), pep + [aa]])
	scorelist = sorted(scorelist, key = lambda x: x[0], reverse = True)
	temp = [x[1] for x in scorelist[:N]]
	for i in range(N, len(scorelist)):
		if scorelist[i][0] == scorelist[N - 1][0]:
			temp.append(scorelist[i][1])
		else:
			break
	peps = temp[:]
	cnt = (cnt + 1) % 8
	maxt = max(sum(pep) for pep in peps)
	print('Running' + '.' * cnt + '\n%.2f%%'% (100 * maxt / maxe) + '\n' * 7)
print('\n'.join(['-'.join(list(map(lambda x: str(x), pep))) for pep in peps]))