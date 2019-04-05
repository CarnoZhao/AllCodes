import random
from collections import defaultdict
from copy import deepcopy

e_spec = list(map(lambda x: eval(x), '371.5 375.4 390.4 392.2 409.0 420.2 427.2 443.3 446.4 461.3 471.4 477.4 491.3 505.3 506.4 519.2 536.1 546.5 553.3 562.3 588.2 600.3 616.2 617.4 618.3 633.4 634.4 636.2 651.5 652.4 702.5 703.4 712.5 718.3 721.0 730.3 749.4 762.6 763.4 764.4 779.6 780.4 781.4 782.4 797.3 862.4 876.4 877.4 878.6 879.4 893.4 894.4 895.4 896.5 927.4 944.4 975.5 976.5 977.4 979.4 1005.5 1007.5 1022.5 1023.7 1024.5 1039.5 1040.3 1042.5 1043.4 1057.5 1119.6 1120.6 1137.6 1138.6 1139.5 1156.5 1157.6 1168.6 1171.6 1185.4 1220.6 1222.5 1223.6 1239.6 1240.6 1250.5 1256.5 1266.5 1267.5 1268.6'.split(' ')))
err = 0.2
masstable = []
f = open('integer_mass_table.txt')
for l in f:
	masstable.append(eval(l.rstrip().split(' ')[1]))
f.close()
lenth = len(e_spec)
masstable2 = list(map(lambda x: eval(x), set('99-128-113-147-97-186-147-114-128-163'.split('-'))))
print(masstable2)
#prepare data

def ChangeConv(masstable, x):
	ret = 0
	mindiv = 200
	for aa in masstable:
		div = abs(x - aa)
		if div < mindiv:
			mindiv = div
			ret = aa
	return ret, mindiv

itertime = 100000
mintotaldiv = 2 ** 31 - 1
for i in range(itertime):
	print('%.3f%%' % (100 * i / itertime) + '\n' * 8)
	for i, x in enumerate(e_spec):
		if x % 1 <= err or x % 1 >= 1 - err:
			e_spec[i] = round(x)
		else:
			e_spec[i] = int(x) if random.random() < 0.5 else int(x) + 1
	#prepare e_spec
	conv = defaultdict(int)
	for i in range(lenth):
		for j in range(i + 1, lenth):
			diff = e_spec[j] - e_spec[i]
			if diff >= 54 and diff <= 189:
				conv[diff] += 1
	#make conv
	totaldiv = 0
	changeconv = defaultdict(int)
	for x in conv:
		#newx, div = ChangeConv(masstable, x)
		newx, div = ChangeConv(masstable2, x)
		changeconv[newx] += conv[x]
		totaldiv += div * conv[x]
	totaldiv /= sum(conv.values())
	changeconv = dict(sorted(changeconv.items(), key = lambda x: x[1], reverse = True))
	if totaldiv < mintotaldiv:
		mintotaldiv = totaldiv
		bestconv = deepcopy(changeconv)
		bestspec = deepcopy(e_spec)
print(mintotaldiv)
print('Myans:', sorted(list(bestconv.keys())[:20]))
print('Ideal:', sorted(map(lambda x: eval(x), set('99-128-113-147-97-186-147-114-128-163'.split('-')))))
f = open('Predata.txt')
mttd = eval(f.readline())
f.close()
if mintotaldiv < mttd:
	#fw = open('Predata.txt', 'w')
	fw = open('Predata2.txt', 'w')
	fw.write(str(mintotaldiv) + '\n')
	fw.write(str(sorted(list(bestconv.keys())[:20])) + '\n')
	fw.write(str(bestspec))
	fw.close()
	print('Written!!')
#99-128-113-147-97-186-147-114-128-163