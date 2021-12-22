import pyautogui
from time import sleep
from pynput.keyboard import Key, Listener
from threading import Thread

locked = False

def stop_autoclicker():
    print("Stopping autoclicker...")
    exit()

def autoclicker():
    for i in range(10):
        pyautogui.leftClick()
        print("clicked")
        sleep(1)
    stop_autoclicker()

def on_press(key):
    global locked
    if key == Key.space and not locked:
        print("Starting autoclicker...")
        autoclicker_thread = Thread(target=autoclicker)
        locked = True
        autoclicker_thread.start()
        print("Autoclicker thread started")

def on_release(key):
    if key == Key.esc:
        stop_autoclicker()

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()