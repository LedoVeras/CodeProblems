import pyautogui as py
import pyperclip as clip
import time

py.PAUSE = 0.1

for i in range(2):
    py.moveTo(70, 200)
    py.drag(900, 0, 0.2, button='left')
    py.hotkey("ctrl", "c")
    py.hotkey("alt", "tab")

    py.hotkey("ctrl", "n")
    py.hotkey("ctrl", "s")
    time.sleep(1)
    py.hotkey("ctrl", "v")
    py.write(".js") 
    py.moveTo(1500, 190)
    py.doubleClick()
    py.moveTo(1500, 142)
    py.doubleClick()
    py.press("enter")
    py.moveTo(2375, 1050)
    py.click()

    py.hotkey("ctrl", "shift", "d")
    py.moveTo(1542, 177)
    py.click()
    py.hotkey("ctrl", "v")
    py.hotkey("ctrl", "shift", "e")
    py.hotkey("ctrl", "tab")
    py.hotkey("ctrl", "tab")


    py.hotkey("alt", "tab")
    py.moveTo(70, 200)
    py.scroll(-10000)

    py.moveTo(554, 775)
    py.click()
    py.hotkey("ctrl", "a")
    py.hotkey("ctrl", "c")
    py.hotkey("ctrl", "w")
    py.hotkey("alt", "tab")
    py.hotkey("ctrl", "v")
    py.hotkey("ctrl", "s")

    py.hotkey("ctrl", "shift", "d")
    py.moveTo(1542, 177)
    py.click()
    py.hotkey("ctrl" , "enter")
    py.hotkey("ctrl", "shift", "e")
    py.hotkey("ctrl", "tab")

    time.sleep(4)