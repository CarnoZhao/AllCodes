import win32gui
import time

global ls
ls = []

def output(num, filts):
    name = win32gui.GetWindowText(num)
    # if filts == [] or name in filts:
    rect = win32gui.GetWindowRect(num)
    ls.append((num, name, rect))

def delete(num, extra):
    name = win32gui.GetWindowText(num)
    rect = win32gui.GetWindowRect(num)
    if (num, name, rect) in ls:
        ls.remove((num, name, rect))

def findDiff():
    win32gui.EnumWindows(output, [])
    time.sleep(3)
    win32gui.EnumWindows(delete, None)
    return ls

if __name__ == '__main__':
    pass
