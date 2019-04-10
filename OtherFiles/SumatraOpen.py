import pyautogui as pg
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
        print(rect)
    elif 'DESKTOP' in name:
        rect = win32gui.GetWindowRect(num)
        window_list['terminal'] = rect
    else:
        pass

def change(terminal, sumatra):
    # RealFull, FakeFull, L, R, else
    pg.hotkey('alt', 'tab')
    # focus on terminal
    if terminal == 'RealFull':
        pg.hotkey('win', 'down')
    # quit real-full mode
    if terminal == 'FakeFull':
        pg.hotkey('win', 'left')
    elif terminal in ('R', 'else', 'RealFull'):
        pg.hotkey('win', 'right')
    else:
        pass
    if sumatra == 'R':
        pass
    elif terminal != 'L':
        pg.press('enter')
        pg.hotkey('alt', 'tab')
    else:
        pg.hotkey('alt', 'tab')
        if sumatra != 'L':
            pg.hotkey('win', 'right')
        else:
            pg.hotkey('win', 'left')
        pg.hotkey('alt', 'tab')

def getTruePos(name):
    rect = window_list[name]
    for key, pos in window_size.items():
        if rect == pos:
            return key
    return 'else'

def main():
    getWindowPosition()
    change(getTruePos('terminal'), getTruePos('sumatra'))

if __name__ == '__main__':
    main()

# R: (1489, 0, 3011, 1951), RealFull: (0, 0, 3000, 2000)
# L: (-11, 0, 1511, 1951), FakeFull: (-13, -13, 3013, 1953)
