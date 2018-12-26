num = eval(input())
roma = []
ls = list(str(num))
ls = list(map(eval, ls))
rels = ls[::-1]
letters = [['I','V','X'], ['X','L','C'], ['C','D','M'], ['M']]
for i in range(len(rels)):
    letter = letters[i]
    if rels[i] == 0:
        continue
    elif rels[i] <= 3:
        roma.append(letter[0] * rels[i])
    elif rels[i] == 4:
        roma.append(letter[0] + letter[1])
    elif rels[i] == 5:
        roma.append(letter[1])
    elif rels[i] == 6:
        roma.append(letter[1] + letter[0])
    elif rels[i] <= 8:
        roma.append(letter[1] + (rels[i] - 5) * letter[0])
    else:
        roma.append(letter[0] + letter[2])
roma = ''.join(roma[::-1])
print(roma)