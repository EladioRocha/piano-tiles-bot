import pyautogui
import keyboard

# pyautogui.move(500, 500)
# pyautogui.displayMousePosition()

y = 475
x1 = 510
x2 = 630
x3 = 868

while not keyboard.is_pressed('s'):
  if pyautogui.pixel(x1, y)[0] < 20:
    pyautogui.click(x1, y)
  if pyautogui.pixel(x2, y)[0] < 20:
    pyautogui.click(x2, y)
  if pyautogui.pixel(x3, y)[0] < 20:
    pyautogui.click(x3, y)
  if pyautogui.pixel(x4, y)[0] < 20:
    pyautogui.click(x4, y)

