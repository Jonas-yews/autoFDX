from re import I
from keyboard import play
import pyautogui
from time import sleep
import numpy as np
import cv2
from time import time
import threading
import winsound
import sys
import keyboard

i = 0 #计次变量i
paused = False
reset_i = False  # 标记是否需要重置 i
lock = threading.Lock()  # 线程锁

DEBUG = False
info = 'init'
mark = '+'
cumMode = 2
resRate = 1
opTime = time()

def switchMark():
    global mark
    mark = '-' if mark == '+' else '+'


def log(buf):
    global info
    global mark
    global opTime
    if time() - opTime > 120:
        pyautogui.press('1')
        opTime = time()
    if buf != info:
        opTime = time()
        info = buf
        print(f'\n  {info}', end='')
    else:
        print(f'\r{mark}', end='')
        switchMark()


def match(template_name, ac=0.85):
    
    img = pyautogui.screenshot()
    open_cv_image = np.array(img)

    img_gray = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(f'./{template_name}.png', 0)

    x, y = template.shape[0:2]
    template = cv2.resize(template, (int(y * resRate), int(x *resRate)))

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    w, h = template.shape[::-1]

    if DEBUG:
        print(max_val, max_loc)

    if max_val < ac:
        return None

    return w // 2 + max_loc[0], h // 2 + max_loc[1]

def play_sound():
    # 播放提示音
    winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
    
# def check_input():
#     global paused, reset_i,i
#     while True:
#         if i >= 5:
#             if keyboard.is_pressed('space'):  # 检测是否按下空格键
#                 paused = not paused
#                 if paused:
#                     print("已暂停，请在3秒内按下空格以重置次数或等待3秒后自动继续。")
#                     start_time = time()
#                     while time() - start_time < 3:
#                         keyboard.wait('space')  # 等待空格键的按下
#                         reset_i = True
#                         i = 0
#                         break
#                     else:
#                         print("继续执行")
#             sleep(0.1)  # 等待一段时间再次检查

def start():
    pos = match('start')
    pyautogui.moveTo(pos[0], pos[1])
    pyautogui.leftClick()
    wait(0.1)
    pyautogui.leftClick()


def wait(sec):
    sleep(sec / 2)


def ready_to_cum():
    return match(f'cum{cumMode}')


def ready_to_start():
    return match('start')


def ready_to_finish():
    return match('finish')


def cum():
    pos = match(f'cum{cumMode}')
    pyautogui.moveTo(pos[0], pos[1])
    pyautogui.leftClick()
    wait(0.1)
    pyautogui.leftClick()


def finish():
    pos = match('finish')
    pyautogui.moveTo(pos[0], pos[1])
    pyautogui.leftClick()
    wait(0.1)
    pyautogui.leftClick()
    wait(0.1)

def give():
    win = pyautogui.getWindowsWithTitle('FallenDoll')[0]
    x, y = win.left, win.top
    pyautogui.moveTo(x + 270 * resRate, y + 268 * resRate )
    pyautogui.leftClick()
    wait(0.1)
    pyautogui.moveTo(x + 125 * resRate, y + 330 * resRate )
    wait(0.1)
    pyautogui.leftClick()
    wait(0.1)
    pyautogui.leftClick()
    wait(0.1)
    pyautogui.moveTo(x + 270 * resRate, y + 378 * resRate )
    pyautogui.leftClick()
    wait(0.1)
    pyautogui.moveTo(x + 125 * resRate, y + 400 * resRate )
    wait(0.1)
    pyautogui.leftClick()
    wait(0.1)
    pyautogui.leftClick()
    wait(0.1)



def loop():
    global i 
    while not ready_to_start():
        log('未找到开始')
        wait(0.2)
    while ready_to_start():
        start()
        pyautogui.moveRel(50 * resRate, 50 * resRate)
        log('点击开始')
        wait(0.2)

    while not ready_to_cum():
        log('未能cum')
        wait(0.2)
    while ready_to_cum():
        cum()
        pyautogui.moveRel(50 * resRate, 50 * resRate)
        log('cum')
        wait(0.2)

    while not ready_to_finish():
        log('等待结束')
        wait(0.2)
    while ready_to_finish():
        finish()
        pyautogui.moveRel(50 * resRate, 50 * resRate)
        log('结束')
        wait(0.2)
        with lock:
            i += 1  # 加锁修改 i 的值
        give()


if __name__ == '__main__':
    # threading.Thread(target=check_input).start()  # 启动检查输入的线程
    while True:
        if i >= 5:
            paused = True  # 暂停主循环
            print("\n____________\n已暂停程序，三秒后自动恢复。\n你可以按下空格中止程序")
            play_sound()
            start_time = time()
            space_pressed = False  # 记录空格键是否被按下
            
            while time() - start_time < 5:
                if keyboard.is_pressed('space'):  # 检测空格键是否被按下
                    space_pressed = True
                    print("____________\n已中止程序，等待按下回车键恢复程序")
                    break  # 中止循环，等待下一步操作
                sleep(0.1)  # 每隔0.1秒检查一次键盘输入                          
            
            if space_pressed:
                while True:
                    if keyboard.is_pressed('enter'):  # 检测回车键是否被按下
                        print("____________\n已按下回车键，恢复程序")
                        with lock:
                            i = 0
                            reset_i = True
                        break  # 退出等待回车键循环
                    sleep(0.1)  # 每隔0.1秒检查一次键盘输入
                paused = False  # 继续主循环
            if not space_pressed and time() - start_time >= 5:
                print("____________\n三秒内未按下空格键，继续执行程序")
                with lock:
                    i = 0
                    reset_i = True
                paused = False  # 继续主循环
        loop()



