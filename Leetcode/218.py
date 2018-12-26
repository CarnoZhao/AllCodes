buildings = [[0,5,7],[5,10,7],[5,10,12],[10,15,7],[15,20,7],[15,20,12],[20,25,7]]
from collections import defaultdict
s_heights = defaultdict(list)
e_heights = defaultdict(list)
ret = []
for bdg in buildings:
	s_heights[bdg[0]] += [bdg[2]]
	e_heights[bdg[1]] += [bdg[2]]
poses = sorted(list(set(s_heights.keys()) | set(e_heights.keys())))
h = [0]
for pos in poses:
	if pos in s_heights and pos not in e_heights:
		if max(s_heights[pos]) > max(h):
			ret.append([pos, max(s_heights[pos])])
		h += s_heights[pos]
	elif pos in e_heights and pos not in s_heights:
		for i in e_heights[pos]:
			del h[h.index(i)]
		if max(h) < ret[-1][-1]:
			ret.append([pos, max(h)])
	else:
		for i in e_heights[pos]:
			del h[h.index(i)]
		if max(s_heights[pos]) > max(h) and max(s_heights[pos]) != ret[-1][-1]:
			ret.append([pos, max(s_heights[pos])])
		h += s_heights[pos]
print(ret)
