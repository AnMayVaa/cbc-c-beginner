import os
import openpyxl

template_path = 'references/QuizizzSampleSpreadsheetUpdated_v2.xlsx'
output_dir = 'quizs'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

quizzes = {
    "01_Fundamentals_Quiz.xlsx": [
        ["What is the correct syntax to output 'Hello World' in C?", "Multiple Choice", 'print("Hello World");', 'printf("Hello World");', 'console.log("Hello World");', 'cout << "Hello World";', "", 2, 20, "", ""],
        ["How do you insert single-line comments in C?", "Multiple Choice", "/* comment */", "# comment", "// comment", "<!-- comment -->", "", 3, 20, "", ""],
        ["Which function is the starting point (entry point) of a C program?", "Multiple Choice", "start()", "init()", "main()", "run()", "", 3, 20, "", ""],
        ["What is '#include <stdio.h>' mainly used for?", "Multiple Choice", "Standard input/output functions", "Math calculation functions", "String manipulation", "Creating custom variables", "", 1, 30, "", ""],
        ["Which symbol must be used to end a statement in C?", "Multiple Choice", ".", ":", "!", ";", "", 4, 15, "", ""],
        ["What does '\\n' do when used inside a printf statement?", "Multiple Choice", "Creates a new line", "Prints the letter n", "Inserts a tab space", "Makes a beep sound", "", 1, 20, "", ""],
        ["Which of the following is NOT a valid variable name in C?", "Multiple Choice", "_number", "Number1", "number_1", "1stNumber", "", 4, 20, "", ""],
        ["How do you start a multi-line comment in C?", "Multiple Choice", "/*", "//", "<!--", "#*", "", 1, 15, "", ""],
        ["Who is known as the creator of the C programming language?", "Multiple Choice", "Bill Gates", "Dennis Ritchie", "Steve Jobs", "James Gosling", "", 2, 20, "", ""],
        ["Which brackets are used to define a block of code in C?", "Multiple Choice", "[ ]", "( )", "{ }", "< >", "", 3, 15, "", ""],
    ],
    "02_DataTypes_Quiz.xlsx": [
        ["Which data type is used to store a single text character?", "Multiple Choice", "int", "char", "float", "string", "", 2, 20, "", ""],
        ["What is the correct format specifier for printing an integer?", "Multiple Choice", "%f", "%c", "%d", "%s", "", 3, 20, "", ""],
        ["How much memory does a typical 'int' take in a modern 32-bit/64-bit system?", "Multiple Choice", "1 byte", "2 bytes", "4 bytes", "8 bytes", "", 3, 20, "", ""],
        ["What is the format specifier for printing a float (decimal number)?", "Multiple Choice", "%f", "%d", "%c", "%s", "", 1, 20, "", ""],
        ["Which of the following is NOT a basic, built-in data type in C?", "Multiple Choice", "int", "char", "float", "string", "", 4, 20, "", ""],
        ["Which data type is best used to store numbers with decimals (e.g. 3.14)?", "Multiple Choice", "int", "char", "float", "long", "", 3, 20, "", ""],
        ["What is the value of x if we declare: `int x = 5.9;` ?", "Multiple Choice", "5.9", "6", "5", "Error", "", 3, 30, "", ""],
        ["What is the format specifier for printing a single character?", "Multiple Choice", "%char", "%c", "%s", "%ch", "", 2, 20, "", ""],
        ["What is the memory size of a 'char' data type?", "Multiple Choice", "1 byte", "2 bytes", "4 bytes", "8 bytes", "", 1, 20, "", ""],
        ["Which keyword is used to make a variable unchangeable (constant)?", "Multiple Choice", "final", "constant", "let", "const", "", 4, 20, "", ""],
    ],
    "03_FlowControl_Quiz.xlsx": [
        ["Which statement is used to execute a block of code ONLY if a condition is true?", "Multiple Choice", "switch", "if", "for", "while", "", 2, 15, "", ""],
        ["What is the correct syntax for a basic for loop?", "Multiple Choice", "for (i = 0, i < 10, i++)", "for (i = 0; i < 10; i++)", "for i in range(10)", "for (i++ ; i < 10 ; i = 0)", "", 2, 30, "", ""],
        ["Which keyword is used to exit a loop completely?", "Multiple Choice", "stop", "exit", "return", "break", "", 4, 20, "", ""],
        ["In a switch statement, what keyword acts like 'else' to handle unmatched cases?", "Multiple Choice", "else", "otherwise", "default", "finally", "", 3, 20, "", ""],
        ["What happens if you run `while(1) { ... }` in C?", "Multiple Choice", "It loops exactly once", "It creates an infinite loop", "It gives a syntax error", "It skips the loop", "", 2, 20, "", ""],
        ["Which operator means 'Equal to' in a condition?", "Multiple Choice", "=", "==", "===", "!=", "", 2, 15, "", ""],
        ["Which operator means 'Not Equal' in a condition?", "Multiple Choice", "==", "<>", "=!", "!=", "", 4, 15, "", ""],
        ["Which statement is often used as a cleaner alternative to multiple if-else statements?", "Multiple Choice", "for", "while", "do-while", "switch", "", 4, 20, "", ""],
        ["What does the `continue` keyword do inside a loop?", "Multiple Choice", "Exits the loop completely", "Skips to the next iteration", "Stops the program", "Restarts the program", "", 2, 20, "", ""],
        ["What is the output of this code: `if (0) { printf(\"A\"); } else { printf(\"B\"); }`", "Multiple Choice", "A", "B", "AB", "Error", "", 2, 30, "", ""],
    ],
    "04_Arrays_Functions_Quiz.xlsx": [
        ["How do you correctly declare an array of 5 integers?", "Multiple Choice", "int arr = [5];", "array<int> arr[5];", "int arr[5];", "int arr(5);", "", 3, 30, "", ""],
        ["What is the index of the first element in a C array?", "Multiple Choice", "1", "0", "-1", "Depends on declaration", "", 2, 15, "", ""],
        ["Which of the following is a correct function declaration in C?", "Multiple Choice", "function sum(int a, int b)", "int sum(int a, int b);", "sum(int a, int b) -> int", "def sum(a, b):", "", 2, 30, "", ""],
        ["What keyword is used to send a value back out of a function?", "Multiple Choice", "yield", "send", "give", "return", "", 4, 15, "", ""],
        ["Can a standard C array change its size after it is created?", "Multiple Choice", "Yes, anytime", "No, it is fixed", "Only if it is global", "Only if it is empty", "", 2, 20, "", ""],
        ["How do you access the 3rd element in the array `int arr[5];`?", "Multiple Choice", "arr[3]", "arr(3)", "arr[2]", "arr.get(3)", "", 3, 30, "", ""],
        ["What happens if you try to access an array out of its bounds (e.g., index 10)?", "Multiple Choice", "Syntax Error", "Returns 0", "Undefined behavior / crash", "Auto-resizes the array", "", 3, 30, "", ""],
        ["A function that does NOT return any value should use which return type?", "Multiple Choice", "null", "empty", "none", "void", "", 4, 20, "", ""],
        ["Inside a `void myFunc()` function, is it legal to use `return;` ?", "Multiple Choice", "Yes, to exit the function", "No, it causes an error", "Yes, but it must be return 0", "Yes, to restart the function", "", 1, 30, "", ""],
        ["What special character is automatically placed at the end of a C string array?", "Multiple Choice", "\\n (Newline)", "\\0 (Null Terminator)", "EOF", "Space character", "", 2, 20, "", ""],
    ]
}

for filename, rows in quizzes.items():
    wb = openpyxl.load_workbook(template_path)
    ws = wb.active
    
    # Delete sample rows (row 3 onwards, row 1 is header, row 2 is instructions)
    ws.delete_rows(3, 100)
    
    # Append new rows starting at row 3
    for r_idx, row_data in enumerate(rows, start=3):
        for c_idx, val in enumerate(row_data, start=1):
            ws.cell(row=r_idx, column=c_idx, value=val)
            
    out_path = os.path.join(output_dir, filename)
    wb.save(out_path)
    print(f"Generated {out_path}")
