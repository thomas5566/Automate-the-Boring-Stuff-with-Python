import subprocess, os, pyautogui, time
import pygetwindow as gw

n = 10
for i in range(n):
    timeformat = 'Launching TAMIS in 00:{:02d}'.format(n)
    print(timeformat, end='\r')
    time.sleep(1)
    n -= 1

os.chdir("C:\WINDOWS\system32")
Quellpfad = r"C:\cwin"
Quelldatei = r"\tamis_wls.bat"
Quelle = Quellpfad + Quelldatei
print(Quelle)
subprocess.Popen(Quelle, shell=True)
time.sleep(3)
win = gw.getWindowsWithTitle('TAMIS-GUI-WLS')[0]
win.activate()
time.sleep(2)
# pyautogui.click(86, 240)
# time.sleep(2)
pyautogui.write('OR' + '\t')
time.sleep(2)
pyautogui.write('OR' + '\t')
time.sleep(2)
pyautogui.write('\n')
time.sleep(2)
pyautogui.doubleClick(105, 303)
time.sleep(2)
pyautogui.click(118, 34)
time.sleep(2)
pyautogui.click(160, 175)



