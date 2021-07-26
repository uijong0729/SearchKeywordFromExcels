from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

# 8번째 줄에 있는 데이터 삭제
ws.delete_rows(8)

# 8번째 줄부터 2줄 데이터 삭제
ws.delete_rows(8, 2)

# 2번째 열(B) 삭제
ws.delete_rows(2)

# 2번째 열(B)로 부터 총 2열 삭제
ws.delete_rows(2, 2)

wb.save("sample_delete_rows.xlsx")
wb.close()