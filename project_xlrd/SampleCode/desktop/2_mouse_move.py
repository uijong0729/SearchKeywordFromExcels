import pyautogui

# 지정한 좌표로 마우스 이동
pyautogui.moveTo(100, 100)
print(pyautogui.position())

# 1.25초 동안 (100, 500)의 위치로 이동
pyautogui.moveTo(100, 500, duration=1.25)
print(pyautogui.position())

# 1.75초 동안 현재 커서 위치에서 상대 좌표로 이동
pyautogui.move(500, 500, duration=1.75)
p = pyautogui.position()
print(p[0], p[1])
print(p.x, p.y)


