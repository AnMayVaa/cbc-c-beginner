import openpyxl

template_path = 'preferences/Blooket_Spreadsheet_Import_Template-CRBqcEp3.xlsx'

quizzes = {
    "01_Fundamentals_Quiz.xlsx": [
        [1, "What is the correct syntax to output 'Hello World' in C?", 'print("Hello World");', 'printf("Hello World");', 'console.log("Hello World");', 'cout << "Hello World";', 20, 2],
        [2, "How do you insert single-line comments in C?", "/* comment */", "# comment", "// comment", "<!-- comment -->", 20, 3],
        [3, "Which function is the entry point of a C program?", "start()", "init()", "main()", "run()", 20, 3],
        [4, "What is '#include <stdio.h>' used for?", "To include standard input/output library", "To include math functions", "To include string functions", "To define variables", 20, 1],
        [5, "Which symbol is used to end a statement in C?", ".", ":", "!", ";", 15, 4],
    ],
    "02_DataTypes_Quiz.xlsx": [
        [1, "Which data type is used to store text characters?", "int", "char", "float", "string", 20, 2],
        [2, "What is the correct format specifier for an integer?", "%f", "%c", "%d", "%s", 20, 3],
        [3, "How much memory does a typical 'int' take in a 32-bit system?", "1 byte", "2 bytes", "4 bytes", "8 bytes", 20, 3],
        [4, "What is the format specifier for a float?", "%f", "%d", "%lf", "%i", 20, 1],
        [5, "Which of the following is NOT a basic data type in C?", "int", "char", "float", "string", 20, 4],
    ],
    "03_FlowControl_Quiz.xlsx": [
        [1, "Which statement is used to execute a block of code if a condition is true?", "switch", "if", "for", "while", 15, 2],
        [2, "What is the correct syntax for a for loop?", "for (i = 0, i < 10, i++)", "for (i = 0; i < 10; i++)", "for i in range(10)", "for (i++ ; i < 10 ; i = 0)", 30, 2],
        [3, "Which keyword is used to exit a loop early?", "stop", "exit", "return", "break", 20, 4],
        [4, "In a switch statement, what is used to handle unspecified cases?", "else", "otherwise", "default", "finally", 20, 3],
        [5, "What will 'while(1)' do in C?", "Loop once", "Create an infinite loop", "Syntax error", "Skip the loop", 20, 2],
    ],
    "04_Arrays_Functions_Quiz.xlsx": [
        [1, "How do you declare an array of 5 integers?", "int arr = [5];", "array<int> arr[5];", "int arr[5];", "int arr(5);", 30, 3],
        [2, "What is the index of the first element in an array?", "1", "0", "-1", "Depends on declaration", 15, 2],
        [3, "Which of the following is a correct function declaration?", "function sum(int a, int b)", "int sum(int a, int b);", "sum(int a, int b) -> int", "def sum(a, b):", 30, 2],
        [4, "What keyword is used to return a value from a function?", "yield", "send", "give", "return", 15, 4],
        [5, "Can a standard C array size be changed after it is created?", "Yes", "No", "Only if it is global", "Only if it is filled", 20, 2],
    ]
}

for filename, rows in quizzes.items():
    wb = openpyxl.load_workbook(template_path)
    ws = wb.active
    
    # The template might have dummy rows from row 3 downwards.
    # Let's just delete rows 3 to 100 just to be safe.
    ws.delete_rows(3, 100)
    
    # Append new rows starting at row 3
    for r_idx, row_data in enumerate(rows, start=3):
        for c_idx, val in enumerate(row_data, start=1):
            ws.cell(row=r_idx, column=c_idx, value=val)
            
    wb.save(filename)
    print(f"Generated {filename}")
