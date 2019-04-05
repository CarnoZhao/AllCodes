import numpy as np
import matplotlib.pyplot as plt

with open('Nums.txt') as f:
		line = f.readline()
		line = list(map(lambda x: eval(x), line[:-1].split('\t')))
		f.close()
minv = min(line)
maxv = max(line)
for i in range(len(line)):
	line[i] = int((line[i] - minv) * -255 / (maxv - minv)) + 255
im0 = np.reshape(line, (20, 20))
print(im0)
plt.imshow(im0, cmap = 'gray')
plt.xticks([]), plt.yticks([])
plt.show()