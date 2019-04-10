import pyautogui
import time
import win32gui

global window_list
window_list = {}
window_size = {
        'R': (1489, 0, 3011, 1951),
        'L': (-11, 0, 1511, 1951),
        'RealFull': (0, 0, 3000, 2000),
        'FakeFull': (-13, -13, 3013, 1953)
        }

def getWindowPosition():
    win32gui.EnumWindows(output, None)

def output(num, extra):
    name = win32gui.GetWindowText(num)
    if 'SumatraPDF' in name:
        rect = win32gui.GetWindowRect(num)
        window_list['sumatra'] = rect
    elif 'DESKTOP' in name:
        rect = win32gui.GetWindowRect(num)
        window_list['terminal'] = rect
    else:
        pass

def change_1():
    '''
    When terminal is full-screen and Sumatra is not open or is open with full screen
    
    '''
    pyautogui.hotkey('alt', 'tab')
    pyautogui.hotkey('win', 'down')
    pyautogui.hotkey('win', 'right')
    pyautogui.press('enter')
    pyautogui.hotkey('alt', 'tab')

def change_2():
    '''
    When terminal is full-screen and Sumatra is open with half screen
    '''
    pyautogui.hotkey('alt', 'tab')
    pyautogui.hotkey('win', 'down')
    pyautogui.hotkey('win', 'right')
    pyautogui.hotkey('alt', 'tab')

def getTruePos(name):
    rect = window_list[name]
    for key, pos in window_size.items():
        if rect == pos:
            return key
    return 'else'


def main()
    getWindowPosition()
    if getTruePos('terminal') == 'RealFull' and getTruePos('sumatra') == 'FakeFull':
        change_1()
    elif 

if __name__ == '__main__':
    getWindowPosition()

# R: (1489, 0, 3011, 1951), RealFull: (0, 0, 3000, 2000)
# L: (-11, 0, 1511, 1951), FakeFull: (-13, -13, 3013, 1953)
