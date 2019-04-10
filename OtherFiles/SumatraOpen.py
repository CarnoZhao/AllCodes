import pyautogui
import time
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
    pass

change_1()


