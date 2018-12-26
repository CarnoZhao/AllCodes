e_spec = list(map(lambda x: eval(x), '371.5 375.4 390.4 392.2 409.0 420.2 427.2 443.3 446.4 461.3 471.4 477.4 491.3 505.3 506.4 519.2 536.1 546.5 553.3 562.3 588.2 600.3 616.2 617.4 618.3 633.4 634.4 636.2 651.5 652.4 702.5 703.4 712.5 718.3 721.0 730.3 749.4 762.6 763.4 764.4 779.6 780.4 781.4 782.4 797.3 862.4 876.4 877.4 878.6 879.4 893.4 894.4 895.4 896.5 927.4 944.4 975.5 976.5 977.4 979.4 1005.5 1007.5 1022.5 1023.7 1024.5 1039.5 1040.3 1042.5 1043.4 1057.5 1119.6 1120.6 1137.6 1138.6 1139.5 1156.5 1157.6 1168.6 1171.6 1185.4 1220.6 1222.5 1223.6 1239.6 1240.6 1250.5 1256.5 1266.5 1267.5 1268.6'.split(' ')))
err = 0.3
#masstable = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 132, 137, 147, 156, 163, 186]
masstable = [99, 128, 113, 147, 97, 186, 114, 163, 132]

lenth = len(e_spec)
aanum = len(masstable)
#target = e_spec[-1]
fw = open('ProteinNode.txt', 'w')
for idx1 in range(lenth):
	target = e_spec[idx1]
	#if idx1 > 4:
	#	break
	cnt = 0
	for i in range(aanum):
		target2 = target + masstable[i]
		for idx2 in range(idx1 + 1, lenth):
			specnum = e_spec[idx2]
			diff = target2 - specnum
			if target2 > specnum - err and target2 < specnum + err:
				print('from %.1f, \t+%d, \tto %.1f, \tdiff = %.1f' % (target, masstable[i], specnum, diff))
				fw.write('%.1f\t%d\t%.1f\n' % (target, masstable[i], specnum))
				cnt += 1
	print('idx1 = %d, cnt = %d' % (idx1, cnt))
fw.close()