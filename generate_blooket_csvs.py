import pandas as pd

# Define headers for Blooket
headers = ["Question Text", "Answer 1", "Answer 2", "Answer 3", "Answer 4", "Time Limit (sec)", "Correct Answer(s)"]

quizzes = {
    "01_Fundamentals_Quiz.csv": [
        ["What is the correct syntax to output 'Hello World' in C?", 'print("Hello World");', 'printf("Hello World");', 'console.log("Hello World");', 'cout << "Hello World";', 20, 2],
        ["How do you insert single-line comments in C?", "/* comment */", "# comment", "// comment", "<!-- comment -->", 20, 3],
        ["Which function is the entry point of a C program?", "start()", "init()", "main()", "run()", 20, 3],
        ["What is '#include <stdio.h>' used for?", "To include standard input/output library", "To include math functions", "To include string functions", "To define variables", 20, 1],
        ["Which symbol is used to end a statement in C?", ".", ":", "!", ";", 15, 4],
    ],
    "02_DataTypes_Quiz.csv": [
        ["Which data type is used to store text characters?", "int", "char", "float", "string", 20, 2],
        ["What is the correct format specifier for an integer?", "%f", "%c", "%d", "%s", 20, 3],
        ["How much memory does a typical 'int' take in a 32-bit system?", "1 byte", "2 bytes", "4 bytes", "8 bytes", 20, 3],
        ["What is the format specifier for a float?", "%f", "%d", "%lf", "%i", 20, 1],
        ["Which of the following is NOT a basic data type in C?", "int", "char", "float", "string", 20, 4],
    ],
    "03_FlowControl_Quiz.csv": [
        ["Which statement is used to execute a block of code if a condition is true?", "switch", "if", "for", "while", 15, 2],
        ["What is the correct syntax for a for loop?", "for (i = 0, i < 10, i++)", "for (i = 0; i < 10; i++)", "for i in range(10)", "for (i++ ; i < 10 ; i = 0)", 30, 2],
        ["Which keyword is used to exit a loop early?", "stop", "exit", "return", "break", 20, 4],
        ["In a switch statement, what is used to handle unspecified cases?", "else", "otherwise", "default", "finally", 20, 3],
        ["What will 'while(1)' do in C?", "Loop once", "Create an infinite loop", "Syntax error", "Skip the loop", 20, 2],
    ],
    "04_Arrays_Functions_Quiz.csv": [
        ["How do you declare an array of 5 integers?", "int arr = [5];", "array<int> arr[5];", "int arr[5];", "int arr(5);", 30, 3],
        ["What is the index of the first element in an array?", "1", "0", "-1", "Depends on declaration", 15, 2],
        ["Which of the following is a correct function declaration?", "function sum(int a, int b)", "int sum(int a, int b);", "sum(int a, int b) -> int", "def sum(a, b):", 30, 2],
        ["What keyword is used to return a value from a function?", "yield", "send", "give", "return", 15, 4],
        ["Can a standard C array size be changed after it is created?", "Yes", "No", "Only if it is global", "Only if it is filled", 20, 2],
    ]
}

for filename, data in quizzes.items():
    df = pd.DataFrame(data, columns=headers)
    df.to_csv(filename, index=False)
    print(f"Generated {filename}")
