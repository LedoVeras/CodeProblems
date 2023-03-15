import pyautogui as py
import pyperclip as clip
import time

py.PAUSE = 0.2


py.moveTo(70, 200)
py.drag(900, 0, 0.2, button='left')
py.hotkey("ctrl", "c")
py.hotkey("alt", "tab")


py.hotkey("ctrl", "alt", "n")
py.hotkey("ctrl", "v")
py.write(".js") 
py.hotkey("ctrl", "shift", "d")
py.moveTo(1542, 177)
py.click()
py.hotkey("ctrl", "v")
py.hotkey("ctrl", "enter")


py.hotkey("alt", "tab")
py.moveTo(70, 200)
py.scroll(-10000)

py.moveTo(554, 775)
py.click()
py.hotkey("ctrl", "a")
py.hotkey("ctrl", "c")
py.hotkey("alt", "tab")




time.sleep(4)
print(py.position())