with open('D:/Browser Download/dataset_9_3.txt') as f:
	text1 = f.readline().rstrip()
	text2 = f.readline().rstrip()
	f.close()
cnt = 0
for i in range(len(text1)):
	if text1[i] != text2[i]:
		cnt += 1
print(cnt)