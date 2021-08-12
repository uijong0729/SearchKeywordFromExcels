# pip install pyautogui
import pyautogui

# 현재 화면의 스크린 사이즈
size = pyautogui.size()

# 가로
print(size[0])
# 세로 
print(size[1])