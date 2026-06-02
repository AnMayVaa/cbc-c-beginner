import os
import openpyxl

template_path = r'C:\Antigravity\CBC C Beginner\references\QuizizzSampleSpreadsheetUpdated_v2.xlsx'
output_dir = r'C:\Antigravity\CBC C Beginner\quizs'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

quizzes = {
    "01_Fundamentals_Quiz.xlsx": [
        ["What is the correct syntax to output 'Hello World' in C?", "Multiple Choice", 'printf("Hello World");', 'print("Hello World");', 'console.log("Hello World");', 'cout << "Hello World";', "", 1, 15, "", ""],
        ["How do you insert a single-line comment in C?", "Multiple Choice", "/* comment */", "# comment", "// comment", "<!-- comment -->", "", 3, 15, "", ""],
        ["Which function is the entry point of every C program?", "Multiple Choice", "start()", "init()", "main()", "run()", "", 3, 15, "", ""],
        ["What is '#include <stdio.h>' used for?", "Multiple Choice", "To include math functions", "To include standard input/output", "To include string functions", "To define variables", "", 2, 20, "", ""],
        ["Which symbol is required to end a statement in C?", "Multiple Choice", ".", ":", "!", ";", "", 4, 15, "", ""],
        ["How do you write a multi-line comment?", "Multiple Choice", "/* comment */", "// comment //", "<!-- comment -->", "''' comment '''", "", 1, 15, "", ""],
        ["What does the '\\n' character do in C?", "Multiple Choice", "Prints a backslash", "Creates a new line", "Inserts a tab space", "Deletes the last character", "", 2, 15, "", ""],
        ["C is known as what type of language?", "Multiple Choice", "Interpreted", "Markup", "Compiled", "Styling", "", 3, 20, "", ""],
        ["What statement typically ends the main() function?", "Multiple Choice", "return 0;", "break;", "end;", "stop();", "", 1, 15, "", ""],
        ["Which symbols define a block of code in C?", "Multiple Choice", "( )", "[ ]", "{ }", "< >", "", 3, 15, "", ""],
    ],
    "02_DataTypes_Quiz.xlsx": [
        ["Which data type is used to store text characters?", "Multiple Choice", "string", "char", "text", "letter", "", 2, 15, "", ""],
        ["What is the format specifier for printing an integer?", "Multiple Choice", "%f", "%c", "%d", "%s", "", 3, 15, "", ""],
        ["What is the format specifier for a float?", "Multiple Choice", "%f", "%d", "%lf", "%i", "", 1, 15, "", ""],
        ["What is the format specifier for a single character?", "Multiple Choice", "%s", "%char", "%c", "%d", "", 3, 15, "", ""],
        ["How much memory does a 'char' normally take?", "Multiple Choice", "1 byte", "2 bytes", "4 bytes", "8 bytes", "", 1, 15, "", ""],
        ["Which of the following is NOT a standard data type in C?", "Multiple Choice", "int", "char", "float", "string", "", 4, 20, "", ""],
        ["Which data type is used for double precision floating-point numbers?", "Multiple Choice", "float2", "double", "real", "long float", "", 2, 15, "", ""],
        ["How do you assign the letter A to a char variable?", "Multiple Choice", 'char x = "A";', "char x = A;", "character x = 'A';", "char x = 'A';", "", 4, 20, "", ""],
        ["In C99 and later, what is the type for true/false values?", "Multiple Choice", "boolean", "bool", "logical", "bit", "", 2, 20, "", ""],
        ["Which type should be used for decimal numbers like 3.14?", "Multiple Choice", "int", "float", "char", "void", "", 2, 15, "", ""],
    ],
    "03_FlowControl_Quiz.xlsx": [
        ["Which statement executes code only if a condition is true?", "Multiple Choice", "if", "switch", "for", "while", "", 1, 15, "", ""],
        ["What is the correct syntax for a 'for' loop?", "Multiple Choice", "for (i = 0, i < 5, i++)", "for (i = 0; i < 5; i++)", "for i in range(5)", "for (i++ ; i < 5 ; i = 0)", "", 2, 30, "", ""],
        ["Which keyword is used to exit a loop early?", "Multiple Choice", "stop", "exit", "return", "break", "", 4, 15, "", ""],
        ["Which keyword skips the rest of the current loop iteration?", "Multiple Choice", "skip", "continue", "pass", "jump", "", 2, 15, "", ""],
        ["In a switch statement, what handles cases that do not match?", "Multiple Choice", "else", "otherwise", "default", "finally", "", 3, 20, "", ""],
        ["What is the correct syntax for a while loop?", "Multiple Choice", "while x < 5:", "while (x < 5)", "loop (x < 5)", "while (x < 5) do", "", 2, 15, "", ""],
        ["How do you write 'else if' in C?", "Multiple Choice", "elif", "elseif", "else if", "elsif", "", 3, 15, "", ""],
        ["Which of the following creates an infinite loop?", "Multiple Choice", "while(1)", "while(0)", "for(endless)", "loop(forever)", "", 1, 20, "", ""],
        ["Which loop ALWAYS executes at least once?", "Multiple Choice", "while", "for", "switch", "do-while", "", 4, 20, "", ""],
        ["Which operator checks if two values are equal?", "Multiple Choice", "=", "===", "==", "!=", "", 3, 15, "", ""],
    ],
    "04_Arrays_Functions_Quiz.xlsx": [
        ["How do you declare an array of 5 integers?", "Multiple Choice", "int arr = [5];", "array<int> arr[5];", "int arr[5];", "int arr(5);", "", 3, 30, "", ""],
        ["What is the index of the first element in a C array?", "Multiple Choice", "1", "0", "-1", "Depends on declaration", "", 2, 15, "", ""],
        ["What return type is used if a function does NOT return a value?", "Multiple Choice", "null", "none", "void", "empty", "", 3, 15, "", ""],
        ["What keyword is used to return a value from a function?", "Multiple Choice", "yield", "send", "give", "return", "", 4, 15, "", ""],
        ["How do you access the 3rd element in an array named 'arr'?", "Multiple Choice", "arr[2]", "arr[3]", "arr(2)", "arr.3", "", 1, 20, "", ""],
        ["Can a standard C array size be changed after it is created?", "Multiple Choice", "Yes", "No", "Only if it is global", "Only if it is empty", "", 2, 15, "", ""],
        ["A function declaration (prototype) must end with a:", "Multiple Choice", ":", "}", ".", ";", "", 4, 15, "", ""],
        ["What does 'arr[0] = 10;' do?", "Multiple Choice", "Compares arr[0] to 10", "Declares an array of size 10", "Assigns 10 to the first element", "Deletes the 10th element", "", 3, 20, "", ""],
        ["A function that calls itself is known as:", "Multiple Choice", "Looping", "Recursive", "Repeating", "Infinite", "", 2, 20, "", ""],
        ["For an array of size 'n', what is the last valid index?", "Multiple Choice", "n", "n + 1", "n - 1", "0", "", 3, 15, "", ""],
    ]
}

for filename, rows in quizzes.items():
    wb = openpyxl.load_workbook(template_path)
    ws = wb.active
    
    ws.delete_rows(3, 100)
    
    for r_idx, row_data in enumerate(rows, start=3):
        for c_idx, val in enumerate(row_data, start=1):
            ws.cell(row=r_idx, column=c_idx, value=val)
            
    out_path = os.path.join(output_dir, filename)
    wb.save(out_path)
    print(f"Generated {out_path}")
