from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "MySheet"

# A1 셀에 1이라는 값을 입력
ws["A1"] = 1
ws["A2"] = 2
ws["A3"] = 3
ws["B1"] = 4
ws["B2"] = 5
ws["B3"] = 6
c = ws.cell(column=3, row=1, value=10) # ws["C1"].value = 10 과 동일한 동작 
print(c.value) # A1셀 

print(ws["A1"])         # A1셀의 정보를 출력
print(ws["A1"].value)   # A1셀의 값을 출력
print(ws["Z99"].value)   # 값이 없을 때는 None을 출력

# row = 1, 2, 3, ...
# column = A, B, C, ...
print(ws.cell(row=1, column=1).value) # A1셀 

###################################################################################
# 반복문을 이용해서 랜덤 숫자 채우기
###################################################################################
from random import *

data = 1
for x in range(1, 11):
    for y in range(1, 11):
        # ws.cell(row=x, column=y, value=randint(0, 100))
        ws.cell(row=x, column=y, value=data)
        data += 1 # 파이썬은 증감연산자가 없음

wb.save("sample.xlsx")
wb.close()