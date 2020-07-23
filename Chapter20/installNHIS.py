#!/usr/bin/env python
# -*- encoding: utf8-*-

import subprocess, os, pyautogui, time, shutil
import pygetwindow as gw

from distutils.dir_util import copy_tree
from swinlnk.swinlnk import SWinLnk

def countDown(x):
    n = x
    for i in range(n):
        timeformat = 'Install in {:02d} ...'.format(n)
        print(timeformat, end='\r')
        time.sleep(1)
        n -= 1

countDown(6)

print("Step 1: Installing Oracle Client")
# os.chdir("C:\installNHIS")
Quellpfad = r"\\172.16.67.41\1資訊課表單\install\NHIS\Oracle_Client\11g_client"
Quelldatei = r"\setup.exe"
Quelle = Quellpfad + Quelldatei
print(Quelle)
subprocess.Popen(Quelle, shell=True)

time.sleep(3)
pyautogui.keyDown('ctrl')
time.sleep(0.5)
pyautogui.press('r')
time.sleep(0.5)
pyautogui.keyUp('ctrl')
time.sleep(10)

countDown(50)

# window active
win = gw.getWindowsWithTitle('Oracle')[0]
win.activate()

# first y
time.sleep(3)
pyautogui.keyDown('altright')
time.sleep(0.5)
pyautogui.press('y')
time.sleep(0.5)
pyautogui.keyUp('altright')
time.sleep(10)

# select a
pyautogui.keyDown('altright')
time.sleep(0.5)
pyautogui.press('a')
time.sleep(0.5)
pyautogui.keyUp('altright')
time.sleep(5)

# secend Next
pyautogui.keyDown('altright')
time.sleep(0.5)
pyautogui.press('n')
time.sleep(0.5)
pyautogui.keyUp('altright')
time.sleep(5)

# third Next
pyautogui.keyDown('altright')
time.sleep(0.5)
pyautogui.press('n')
time.sleep(0.5)
pyautogui.keyUp('altright')
time.sleep(5)

# chang path
pyautogui.press('tab', presses=3, interval=0.5)
time.sleep(3)
pyautogui.write('C:\Oracle')
time.sleep(3)

# Next step
pyautogui.keyDown('altright')
time.sleep(0.5)
pyautogui.press('n')
time.sleep(0.5)
pyautogui.keyUp('altright')
time.sleep(10)

# conplite f
pyautogui.keyDown('altright')
time.sleep(0.5)
pyautogui.press('f')
time.sleep(0.5)
pyautogui.keyUp('altright')
# installation
countDown(200)

# #Firewall window active
# win = gw.getWindowsWithTitle('Windows')[0]
# win.activate()
# pyautogui.keyDown('altright')
# time.sleep(0.5)
# pyautogui.press('r')
# time.sleep(0.5)
# pyautogui.keyDown('altright')
# time.sleep(0.5)
# pyautogui.press('a')
# time.sleep(0.5)
# pyautogui.keyUp('altright')
# time.sleep(10)

# finish Quite
pyautogui.keyDown('altright')
time.sleep(0.5)
pyautogui.press('c')
time.sleep(0.5)
pyautogui.keyUp('altright')

print("Step 2 : Copy tnsnames to C:\\Oracle...\\admin\\...")
countDown(5)
copytnsnames = r"\\172.16.67.41\1資訊課表單\install\NHIS\tnsnames.ora"
destinationloca = r"C:\Oracle\product\11.2.0\client_1\network\admin"
shutil.copy2(copytnsnames, destinationloca)

print("Step 3 : Copy NHIS file to C Disk...")
countDown(5)
fromDirectiory = r"\\172.16.67.41\1資訊課表單\install\NHIS\NHIS"
toDirctory = r"C:\NHIS"
copy_tree(fromDirectiory, toDirctory)

print("Step 4 : Copy NHIS Link to desktop...")
countDown(5)
hisLinkd = r"C:\NHIS"
hisLinkicon = r"\HIS.exe - 捷徑.lnk"
hispath = hisLinkd + hisLinkicon
# str_utf8 = hispath.encode('UTF-8', 'strict')
# ch_hispath = str_utf8.decode('UTF-8', 'strict')

desktopicon = r"C:\Users\winxp\desktop"
# swl = SWinLnk()
# swl.create_lnk(ch_hispath, desktopicon)
shutil.copy2(hispath, desktopicon)

os.system("pause")




