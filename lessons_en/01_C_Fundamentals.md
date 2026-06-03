# Module 1: Fundamentals of C Programming

Welcome to the Computer Boost Camp! In this camp, we will use the C programming language as a medium to learn programming logic.

## What is C?
C is a fast programming language that serves as the foundation for many modern languages. Writing C code requires a **Compile** process to convert our human-readable code into a format that the computer understands (a popular tool for this is the GCC Compiler).

However, to make learning easier, we will write and run our code using an Online Compiler.
> We recommend using the **[Programiz C Online Compiler](https://www.programiz.com/c-programming/online-compiler/)** alongside reading this material.

---

## Basic Structure
The main structure of a C program looks like this. Everything we want the computer to execute must always be inside the `main function`.

```c
#include <stdio.h> // Import the standard input/output library

// The entry point of the program
int main() {
    
    // Write our code here
    
    return 0; // End the execution of the main function
}
```

> **Warning:** Most statements in C must end with a semicolon `;`. If you forget it, the program will throw an Error and will not run.

---

## Outputting with `printf`
We use the `printf` (Print Formatted) command to display text on the screen.

```c
#include <stdio.h>

int main() {
    printf("Hello CBC Boost Camp!\n"); // \n (Backslash n) is used to create a new line
    
    printf("My name is ...\n");
    return 0;
}
```

### Exercise 1.1: Hello Wide World
Take the code above and run it in the Programiz web compiler, then:
1. Change `My name is ...` to your own nickname.
2. Add another `printf` command to print your favorite food on a new line.

---

## Getting Input with `scanf`
We use the `scanf` (Scan Formatted) command to receive data typed in by the user.

```c
#include <stdio.h>

int main() {
    int age; // Create a variable to wait and receive age (as a whole number)
    
    printf("How old are you?: "); 
    
    // For scanf, you must use & (Ampersand) in front of the variable name to point to its memory address
    scanf("%d", &age); 
    
    printf("Wow, you are %d years old!\n", age);
    return 0;
}
```

### Exercise 1.2: Birth Year Calculator
Write a program that asks for a **Birth Year (A.D.)** and let the computer **calculate the age**.
*(Hint: Create a variable to receive the birth year, then compute `2026 - birth year` and display the result)*

### Exercise 1.3: Personal Profile File
Write a program that asks for "age" and "weight" (receive both as integers) and then display a summary at once.
Example:
```text
Enter your age: 15
Enter your weight: 55
You are 15 years old and your weight is 55!
```
