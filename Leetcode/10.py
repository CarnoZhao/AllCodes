s = input("s = ")
p = input("p = ")

s2 = []
i = -1
while i >= -len(s):
    if i == -1:
        s2.append(1)
    elif s[i] == s[i + 1]:
        s2.append(s2[-1] + 1)
    elif s[i] != s[i + 1]:
        s2.append(1)
    i -= 1
s2 = s2[::-1]

p2 = []
p3 = []
for char in p:
    if char != '*':
        p2.append(char)
        p3.append(0)
    else:
        p3[-1] = 1
i = 0
while i < len(p2) - 1:
    if p2[i] == p2[i + 1] and p3[i] == 1 and p3[i + 1] == 1:
        del p2[i]
        del p3[i]
    else:
        i += 1


i = 0
j = 0 #index of s and p

record = []
retreat = 0
ret = True
while i < len(s) and j < len(p2):
    if (s[i] == p2[j] or p2[j] == '.') and p3[j] == 0:
        i += 1
        j += 1
    elif (s[i] != p2[j] and p2[j] != '.') and p3[j] == 0:
        ret = False
    elif (s[i] == p2[j] or p2[j] == '.') and p3[j] == 1:
        if retreat == 0:
            cnt = 0
            record.append([i, j, cnt])
        else:
            retreat = 0
        i += cnt
        j += 1
    else:
        j += 1

    if i >= len(s) and j < len(p2):
        for k in range(j, len(p2)):
            if p3[k] != 1:
                ret = False
                break
    elif i < len(s) and j >= len(p2):
        ret = False
    if ret == False:
        while len(record) > 0:
            record[-1][-1] += 1
            i, j, cnt = record[-1]
            if (cnt > s2[i] and p2[j] != '.') or \
                (cnt > len(s) - i and p2[j] == '.'):
                del record[-1]
                continue
            else:
                break
        if len(record) == 0:
            break
        else:
            retreat = 1
            ret = True
            continue
for k in range(j, len(p2)):
    if p3[k] != 1:
        ret = False
        break
if i < len(s):
    ret = False
return ret