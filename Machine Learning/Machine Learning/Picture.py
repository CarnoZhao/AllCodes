import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

def all_change(func, im):
	for i in range(h):
		for j in range(w):
			func(im, i, j)

def binary(im, i, j):
	im[i][j] = 0 if im[i][j] < minvalue else 255
	return 0

'''def divide_image(im):
	w = np.size(im, 1)
	span = w // 4
	im1 = im[..., :span]
	im2 = im[..., span: 2* span]
	im3 = im[..., 2 * span: 3 * span]
	im4 = im[..., 3 * span:]
	return im1, im2, im3, im4

def clean_dot(im, i, j):
	if im[i][j] == 0:
		cnt = 0
		if i == 0:
			cnt += 1 + int(im[i + 1][j] != 0)
		elif i == h - 1:
			cnt += 1 + int(im[i - 1][j] != 0)
		else:
			cnt += int(im[i + 1][j] != 0) + int(im[i - 1][j] != 0)
		if j == 0:
			cnt += 1 + int(im[i][j + 1] != 0)
		elif j == w - 1:
			cnt += 1 + int(im[i][j - 1] != 0)
		else:
			cnt += int(im[i][j + 1] != 0) + int(im[i][j - 1] != 0)
		if cnt >= 3:
			im[i][j] = 255
	return 0'''

#for i in range(1):
i = 1
file_name = 'Teacher.png'
im = cv.imread(file_name, 0)
h, w = np.shape(im)
print(h, w)
hist_data = im.flat[:].tolist()
'''plt.hist(hist_data)
plt.show()'''

ls = [0] * (1 + 255 // 10)
for i in range(len(hist_data)):
	ls[hist_data[i] // 10] += 1
ls_bak = ls[:]
i = 0
while i < len(ls):
	if ls[i] < 10:
		del ls[i]
	else:
		i += 1
half = len(ls) // 2
max1 = ls.index(max(ls[:half]))
max2 = ls.index(max(ls[half:]))
minvalue = ls_bak.index(min(ls[max1:max2])) * 10 + 5
all_change(binary, im)
plt.imshow(im, cmap = 'gray')

'''all_change(clean_dot, im)
im1, im2, im3, im4 = divide_image(im)
plt.subplot(221)
plt.imshow(im1, cmap = 'gray')
plt.xticks([]), plt.yticks([])
plt.subplot(222)
plt.imshow(im2, cmap = 'gray')
plt.xticks([]), plt.yticks([])
plt.subplot(223)
plt.imshow(im3, cmap = 'gray')
plt.xticks([]), plt.yticks([])
plt.subplot(224)
plt.imshow(im4, cmap = 'gray')
plt.xticks([]), plt.yticks([])'''

plt.show()