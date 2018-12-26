s = input()
letter = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
num = [1000, 500, 100, 50, 10, 5, 1]
i = 0
ret = 0
while i < len(s):
    idx = letter.index(s[i])
    try:
        idxplus = letter.index(s[i + 1])
    except:
        idxplus = len(letter) - 1
    if idxplus < idx:
        ret += num[idxplus] - num[idx]
        i +=2
    else:
        ret += num[idx]
        i += 1

print(ret)

    