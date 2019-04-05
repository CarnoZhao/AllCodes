n = 2
logs = ["0:start:0",
		 "1:start:2",
		 "1:end:5",
		 "0:end:6"]
from collections import defaultdict
lslogs = list(map(lambda x: [eval(x[0]), int(x[1] == 'start'), eval(x[2])], [x.split(':') for x in logs]))
logs = [0] * n
stack = []
for func in lslogs:
	if func[1] == 1:
		if stack != []:
			logs[stack[-1]] += func[2] - pretime - 1
		stack.append(func[0])
		logs[func[0]] += 1
	else:
		logs[stack[-1]] += func[2] - pretime
		stack.pop()
	pretime = func[2]
print(logs)
