def makeBinary(binarylenth):
	binary = [1]
	for j in range(1, binarylenth + 1):
		binary.append(binary[-1] * (binarylenth - j + 1) // j)
	sumvolume = sum(binary)
	return sumvolume, binary

def fillBlank(mtx, binarylenth, layer, left, binary, sumvolume):
	for in_Pos in range((layer - binarylenth) // 2, (layer + binarylenth) // 2 + 1):
		mtx[layer][in_Pos] = left * binary[in_Pos - (layer - binarylenth) // 2] / sumvolume
	return mtx

class Solution:
	def champagneTower(self, poured, query_row, query_glass):
		mtx = [([0] * (i + 1))[:] for i in range(query_row + 2)]
		layer = 0
		while 2 ** (layer + 1) <= poured + 1:
			layer += 1
		if layer > query_row:
			return 1, mtx
		for i in range(min(layer, query_row)):
			for j in range(i + 1):
				mtx[i][j] = 1
		indicator = poured - 2 ** layer + 1
		left = poured - (layer + 1) * layer // 2 - indicator
		print(left, indicator)
		for binarylenth in range(layer):
			if (binarylenth % 2 - layer % 2) != 0:
				continue
			sumvolume, binary = makeBinary(binarylenth)
			if sumvolume > left:
				mtx = fillBlank(mtx, binarylenth, layer, left, binary, sumvolume)
				break
		for layerpos in range(layer + 1):
			sumvolume, binary = makeBinary(layer)
			mtx[layer][layerpos] += indicator * binary[layerpos] / sumvolume
		while layer <= query_row:
			for layerpos in range(layer + 1):
				if mtx[layer][layerpos] > 1:
					mtx[layer + 1][layerpos] += (mtx[layer][layerpos] - 1) / 2
					mtx[layer + 1][layerpos + 1] += (mtx[layer][layerpos] - 1) / 2
					mtx[layer][layerpos] = 1
			layer += 1
		return mtx[query_row][query_glass], mtx

s = Solution()
ans, mtx = s.champagneTower(31, 10, 10)
print(ans)
for line in mtx:
	print(line)