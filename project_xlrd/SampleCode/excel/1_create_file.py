from openpyxl import Workbook

wb = Workbook()         # 새 워크북 생성
ws = wb.active          # 현재 활성화 된 sheet를 가져 옴
ws.title = "sheet1"     # 워크시트의 이름을 변경
wb.save("sample.xlsx")  # 저장
wb.close()