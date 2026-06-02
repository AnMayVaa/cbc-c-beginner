import openpyxl
import csv

quizzes = [
    "01_Fundamentals_Quiz",
    "02_DataTypes_Quiz",
    "03_FlowControl_Quiz",
    "04_Arrays_Functions_Quiz"
]

for quiz in quizzes:
    wb = openpyxl.load_workbook(f"{quiz}.xlsx", data_only=True)
    ws = wb.active
    
    with open(f"{quiz}_blooket.csv", 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for row in ws.iter_rows(values_only=True):
            # Replace None with empty string
            row_data = ["" if cell is None else str(cell) for cell in row]
            writer.writerow(row_data)
            
    print(f"Generated {quiz}_blooket.csv")
