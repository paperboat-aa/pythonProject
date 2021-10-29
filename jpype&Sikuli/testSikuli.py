import time
import tkinter.messagebox
import unittest

import jpype
import win32api
import win32con
from jpype import *


startJVM(r'C:\Program Files\Java\jre1.8.0_311\bin\server\jvm.dll', '-ea',
         r'-Djava.class.path=G:\sikulix\sikulixapi.jar')
app = JClass('org.sikuli.script.App')
Screen = JClass('org.sikuli.script.Screen')
screen = Screen()
screen.find('/venv/img/1.png')
screen.doubleClick('/venv/img/2.png')
x = screen.exists(r'/venv/img/1.png')
print(x)
time.sleep(1.0)
screen.exists('/venv/img/3.png')
screen.click('/venv/img/4.png')
screen.click('/venv/img/5.png')
screen.type('1324567897')
time.sleep(1.0)
win32api.keybd_event(27, 0, 0, 0)
time.sleep(1.0)
win32api.keybd_event(57, 0, 0, 0)
time.sleep(0.2)
win32api.keybd_event(56, 0, 0, 0)
time.sleep(0.2)
win32api.keybd_event(55, 0, 0, 0)
time.sleep(0.2)
win32api.keybd_event(54, 0, 0, 0)
time.sleep(0.2)
win32api.keybd_event(53, 0, 0, 0)
time.sleep(0.2)
win32api.keybd_event(52, 0, 0, 0)
time.sleep(0.2)
win32api.keybd_event(51, 0, 0, 0)
time.sleep(0.2)
win32api.keybd_event(50, 0, 0, 0)
time.sleep(0.2)
win32api.keybd_event(49, 0, 0, 0)
time.sleep(0.2)
win32api.keybd_event(48, 0, 0, 0)
time.sleep(0.2)
win32api.keybd_event(27, 0, 0, 0)
time.sleep(1.0)
win32api.keybd_event(18, 0, 0, 0)  # 按下
win32api.keybd_event(115, 0, 0, 0)
time.sleep(0.1)  # 延迟一会儿
win32api.keybd_event(18, 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开
win32api.keybd_event(115, 0, win32con.KEYEVENTF_KEYUP, 0)
time.sleep(1.0)
top = tkinter.Tk()
top.geometry('0x0+999999+0')
res = tkinter.messagebox.showinfo('提示', '自动化测试结束！')
top.destroy()
jpype.ShutdownJVM()
