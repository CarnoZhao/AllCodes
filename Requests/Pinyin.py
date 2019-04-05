import pyautogui
w, h = pyautogui.size()

def main():
	pyautogui.hotkey('alt', 'tab')
	with open('Pinyinnames.txt') as f:
		for i in range(0):#已经检查了这么多个了
			f.readline()
		for i in range(1000):#即将检查这些
			name = f.readline().rstrip()
			pyautogui.click((3 / 4) * w, (5 / 13) * h)
			pyautogui.hotkey('ctrl', 'a')
			pyautogui.typewrite(name)
			pyautogui.click((3/ 4) * w, h / 2)
			'''find = pyautogui.locateOnScreen('Pic.png')
			if find == None:
				fw.write(name + '\n')
				break'''
	pyautogui.hotkey('alt', 'tab')
	f.close()

main()