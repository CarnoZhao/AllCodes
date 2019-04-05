import numpy as np
from math import exp, sqrt

def add_column(X):
	return np.hstack((np.ones((np.size(X, 0), 1)), X))

def int_to_list(n):
	ret = np.zeros(10)
	ret[..., n] = 1
	return ret

def sigmoid(X):
	r, c = X.shape
	Y = X.flat
	for i in range(len(Y)):
		Y[i] = 1 / (1 + exp(-Y[i]))
	X = np.reshape(Y, (r, c))
	return X

def random_init(r, c):
	e = sqrt(6 / (r + c))
	ret = np.random.rand(r + 1, c) * 2 * e
	ret = ret - np.ones(np.shape(ret)) * e
	return ret

def data_load(ls):
	trainset = []
	cvset = []
	testset = []
	with open('Nums.txt') as f:
		for i in range(ls[0]):
			line = f.readline()
			line = np.array(list(map(lambda x: eval(x), line[:-1].split('\t'))))
			trainset.append(line)
		trainset = np.array(trainset)
		for i in range(ls[1]):
			line = f.readline()
			line = np.array(list(map(lambda x: eval(x), line[:-1].split('\t'))))
			cvset.append(line)
		cvset = np.array(cvset)
		for i in range(ls[2]):
			line = f.readline()
			line = np.array(list(map(lambda x: eval(x), line[:-1].split('\t'))))
			testset.append(line)
		testset = np.array(testset)
		f.close()
	with open('Labels.txt') as f:
		labels = f.readlines()
		f.close()
	labels = list(map(lambda x: eval(x), labels))
	for i in range(len(labels)):
		labels[i] = int_to_list(labels[i])
	trainlabel = np.array(labels[:ls[0]])
	cvlabel = np.array(labels[ls[0]: ls[0] + ls[1]])
	testlabel = np.array(labels[ls[0] + ls[1]: ls[0] + ls[1] +ls[2]])
	return trainset, cvset, testset, trainlabel, cvlabel, testlabel

def forward_comput(X1, theta1, theta2):
	Z = X1.dot(theta1)
	H = sigmoid(Z)
	H1 = add_column(H)
	A = H1.dot(theta2)
	Y_x = sigmoid(A)
	return H, H1, Y_x

def back_propagation(X1, H, H1, Y_x, Y, alpha, theta1, theta2, lam):
	m = np.size(X1, 0)
	grad2 = (alpha[1] / m) * (H1.T).dot(Y_x * (Y_x - np.ones(np.shape(Y_x))) * (Y_x - Y))
	theta2_1 = theta2[1:, ...]
	E = (Y_x * (Y_x - np.ones(np.shape(Y_x))) * (Y_x - Y)).dot(theta2_1.T)
	grad1 = (alpha[0] / m) * X1.T.dot(H * (np.ones(np.shape(H)) - H) * E)
	theta10 = np.vstack((np.zeros((1, np.size(theta1, 1))), theta1[1:, ...]))
	theta20 = np.vstack((np.zeros((1, np.size(theta2, 1))), theta2[1:, ...]))
	theta1 = theta1 + grad1 - (lam / m) * theta10
	theta2 = theta2 + grad2 - (lam / m) * theta20
	return theta1, theta2
	
def test(x, theta1, theta2):
	x1 = add_column(x)
	H, H1, y = forward_comput(x1, theta1, theta2)
	y = y.tolist()[0]
	for i in range(len(y)):
		if y[i] == max(y):
			y[i] = 1
			index = i
		else:
			y[i] = 0
	return index

def main():
	ls = [3000, 1000, 1000]
	test_times = 1000
	num_hide = 100
	train_times = 5000
	alpha = (1, 1)
	lam = 0.5
	print("Loading Data...")
	X, cvX, tsX, Y, cvY, tsY = data_load(ls)
	theta1 = random_init(np.shape(X)[1], num_hide)
	theta2 = random_init(num_hide, np.shape(Y)[1])
	X1 = add_column(X)
	print("Training...")
	for i in range(train_times):
		H, H1, Y_x = forward_comput(X1, theta1, theta2)
		theta1, theta2 = back_propagation(X1, H, H1, Y_x, Y, alpha, theta1, theta2, lam)
	cnt = 0
	print("Testing...")
	for i in range(test_times):
		x = np.reshape(tsX[i], (1, np.size(tsX, 1)))
		y_num = test(x, theta1, theta2)
		for j in range(len(tsY[i])):
			if tsY[i][j] == 1:
				rnum = j
				break
		if rnum == y_num:
			cnt += 1
	print("\ntheta1 = \n", theta1)
	print("\ntheta2 = \n", theta2)
	print("Accuracy = %.1f%%" % (cnt * 100 / test_times))
	with open('Theta1.txt', 'w') as f:
		for i in range(np.size(theta1, 0)):
			for j in range(np.size(theta1, 1)):
				f.write(str(theta1[i][j]) + "\t")
			f.write("\n")
		f.close()
	with open('Theta2.txt', 'w') as f:
		for i in range(np.size(theta2, 0)):
			for j in range(np.size(theta2, 1)):
				f.write(str(theta2[i][j]) + "\t")
			f.write("\n")
		f.close()

main()