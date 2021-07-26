from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

# 행 삽입에 대한 방법 (밀어내고 삽입)
ws.insert_rows(8)

# 8번째 줄 위치에 5줄을 추가
ws.insert_rows(8, 5)

# B열에 새로운 빈 열을 추가
ws.insert_cols(2)

# B열에 새로운 빈 열을 3열 추가
ws.insert_cols(2, 3)


wb.save("sample_insert_rows.xlsx")
wb.close()