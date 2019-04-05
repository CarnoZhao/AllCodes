TRACK_EX = """\
                                /------------\\
/-------------\\                /             |
|             |               /              S
|             |              /               |
|        /----+--------------+------\\        |   
\\       /     |              |      |        |     
 \\      |     \\              |      |        |                    
 |      |      \\-------------+------+--------+---\\
 |      |                    |      |        |   |
 \\------+--------------------+------/        /   |
        |                    |              /    | 
        \\--------------------+-------------/     |
                             |                   |
/-------------\\              |                   |
|             |              |             /-----+----\\
|             |              |             |     |     \\
\\-------------+--------------+-----S-------+-----/      \\
              |              |             |             \\
              |              |             |             |
              |              \\-------------+-------------/
              |                            |               
              \\----------------------------/ 
"""
TRACK_EX = '''\
    /---------------------\\               /-\\ /-\\  
   //---------------------\\\\              | | | |  
  //  /-------------------\\\\\\             | / | /  
  ||  |/------------------\\\\\\\\            |/  |/   
  ||  ||                   \\\\\\\\           ||  ||   
  \\\\  ||                   | \\\\\\          ||  ||   
   \\\\-//                   | || \\---------/\\--/|   
/-\\ \\-/                    \\-/|                |   
|  \\--------------------------/                |   
\\----------------------------------------------/   
'''
from collections import defaultdict

def makeFull(track):
	linesep = track.split('\n')
	rnum = len(linesep)
	cnum = max([len(line) for line in linesep])
	fullsep = []
	for i in range(rnum + 2):
		if i in (0, rnum + 1):
			fullsep.append([''] * (cnum + 2))
			continue
		fullsep.append([])
		for j in range(cnum + 2):
			if j in (0, cnum + 1):
				fullsep[i].append('')
				continue
			try:
				fullsep[i].append(linesep[i - 1][j - 1])
			except:
				fullsep[i].append('')
	for j in range(cnum + 2):
		if fullsep[1][j] not in ('', ' '):
			startpos = (1, j)
			break
	i, j = startpos
	return i, j, startpos, fullsep

def loadTrack(track):
	i, j, startpos, fullsep = makeFull(track)
	prei, prej = i, j
	dirc = 'r'
	dircdic = {
		'r': (0, 1), 
		'l': (0, -1), 
		'u': (-1, 0), 
		'd': (1, 0), 
		'ru': (-1, 1), 
		'lu': (-1, -1), 
		'rd': (1, 1), 
		'ld': (1, -1)}
	possible = ['-', '|', '/', '\\', '+', 'X', 'S']
	checkdict = {}
	crosslist = defaultdict(list)
	stationlist = []
	cnt = 0
	while True:
		if fullsep[i][j] in ('+', 'X'):
			crosslist[(i, j)].append(cnt)
		elif fullsep[i][j] == 'S':
			stationlist.append(cnt)
			way = 0
			for choosedirc in list(dircdic.keys()):
				nexi, nexj = i + dircdic[choosedirc][0], j + dircdic[choosedirc][1]
				if fullsep[nexi][nexj] in possible:
					way += 1
			if way == 4:
				crosslist[(i, j)].append(cnt)
		for choosedirc in [dirc] + list(dircdic.keys()):
			nexi, nexj = i + dircdic[choosedirc][0], j + dircdic[choosedirc][1]
			if choosedirc in ('u', 'd', 'l', 'r') and fullsep[i][j] in ('/', '\\') and fullsep[nexi][nexj] in ('/', '\\'):
				continue
			elif choosedirc in ('ru', 'rd', 'lu', 'ld') and fullsep[nexi][nexj] in ('-', '|'):
				continue
			elif choosedirc in ('ru', 'ld') and fullsep[nexi][nexj] == '\\':
				continue
			elif choosedirc in ('lu', 'rd') and fullsep[nexi][nexj] == '/':
				continue
			elif choosedirc in ('r', 'l') and fullsep[nexi][nexj] == '|':
				continue
			elif choosedirc in ('u', 'd') and fullsep[nexi][nexj] == '-':
				continue
			if fullsep[nexi][nexj] in possible and (nexi, nexj) != (prei, prej):
				break
		prei, prej, i, j, dirc, cnt = i, j, nexi, nexj, choosedirc, cnt + 1
		if (i, j) == startpos:
			break
	crosslist = dict(crosslist.values())
	for key in list(crosslist.keys()):
		crosslist[crosslist[key]] = key
	return stationlist, crosslist, cnt

def loadTrain(at, bt):
	ret = []
	for train in (at, bt):
		ret.append(len(train))
		ret.append('X' in train)
		ret.append('clock' if train[0] > train[-1] else 'anti')
	return ret

def move(stationlist, lenth, ex, dirc, pos, tracklenth, stop):
	if ex or (not ex and pos not in stationlist) or stop == 0:
		pos = (pos + 1) % tracklenth if dirc == 'clock' else (pos - 1) % tracklenth
		stop = lenth - 1
	else:
		stop -= 1
	return pos, stop

def checkCrash(aposlist, bposlist, crosslist, tracklenth):
	reta, retb = False, False
	for a in aposlist:
		if a in bposlist:
			reta = True
		elif a in crosslist:
			reta = crosslist[a] in aposlist + bposlist
		if reta:
			break
	for b in bposlist:
		if b in aposlist:
			retb = True
		elif b in crosslist:
			retb = crosslist[b] in aposlist + bposlist
		if retb:
			break
	return reta or retb

def getSPEP(pos, lenth, dirc, tracklenth):
	ret = [pos, pos + lenth] if dirc == 'anti' else [pos - lenth + 1, pos + 1]
	ret = [ret[0] % tracklenth, ret[1] % tracklenth]
	if ret[0] > ret[1]:
		ret = list(range(0, ret[1])) + list(range(ret[0], tracklenth))
	else:
		ret = list(range(ret[0], ret[1]))
	return ret

def train_crash(track, a_train, a_train_pos, b_train, b_train_pos, limit):
	#return 0
	#print(a_train, a_train_pos, b_train, b_train_pos, limit)
	crash = False
	stationlist, crosslist, tracklenth = loadTrack(track)
	lena, exa, dirca, lenb, exb, dircb = loadTrain(a_train, b_train)
	stopa, stopb = 1, 1
	for time in range(limit + 1):
		aposlist, bposlist = getSPEP(a_train_pos, lena, dirca, tracklenth), getSPEP(b_train_pos, lenb, dircb, tracklenth)
		crash = checkCrash(aposlist, bposlist, crosslist, tracklenth)
		a_train_pos, stopa = move(stationlist, lena, exa, dirca, a_train_pos, tracklenth, stopa)
		b_train_pos, stopb = move(stationlist, lenb, exb, dircb, b_train_pos, tracklenth, stopb)
		if crash:
			break
	return time if crash else -1

#print(train_crash(TRACK_EX, "Aaaa", 147, "Bbbbbbbbbbb", 288, 1000))
print(train_crash(TRACK_EX, 'aA', 10, 'oooooooooooooooooooooooooO', 70, 200))