height = []
while True:
    a = eval(input())
    if a != -1:
        height.append(a)
    elif a == -1:
        break
maxv = 0
i = 0
j = len(height)
while i != j:
    volume = min(height[i], height[j]) * abs(i - j)
    maxv = max(maxv, volume)
    if height[i] <= height[j]:
        i += 1
    elif height[i] > height[j]:
        j -= 1
print(maxv)
