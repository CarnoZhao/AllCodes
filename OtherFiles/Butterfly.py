import cv2
import numpy as np
import matplotlib.pyplot as plt

fig = cv2.cvtColor(cv2.imread('D:/Onedrive - mails.ucas.edu.cn/butterfly.jpg'), cv2.COLOR_BGR2GRAY)
plt.hist(fig.ravel())
plt.show()
#cv2.imshow('1', fig)
#cv2.waitKey()