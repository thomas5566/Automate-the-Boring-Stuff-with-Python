import pyautogui, pyperclip
import pygetwindow as gw

p = pyautogui.confirm('Please open Notpad++ first!!')

if p == 'OK':
    win = gw.getWindowsWithTitle('Notepad++')[0]
    win.activate()
    pyautogui.click(280, 336)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    word = pyperclip.paste()
    print(word)

