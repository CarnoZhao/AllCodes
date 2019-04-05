import pyautogui
w, h = pyautogui.size()

def main():
	pyautogui.hotkey('alt', 'tab')
	while True:
		pyautogui.press(['a', 'right'])

main()