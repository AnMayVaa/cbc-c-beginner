# Module 2: Data Types and Variables

A variable is a space in memory that we reserve to store data. We must define the correct data type so the computer can allocate memory appropriately.

## Basic Data Types in C
- `int` (Integer) is used to store **whole numbers** (e.g., 5, -10, 1000).
- `float` (Floating point) is used to store **decimal numbers** (e.g., 3.14, -0.01).
- `char` (Character) is used to store **a single character** (enclosed in single quotes `' '` e.g., `'A'`, `'z'`).

| Data Type | Memory Size | Range (Approximate) |
| --- | --- | --- |
| `int` | 4 bytes | -2,147,483,648 to 2,147,483,647 |
| `float` | 4 bytes | About 6-7 decimal places |
| `char` | 1 byte | 1 character |

### Variable Naming Rules
1. No spaces allowed (you can use `_` instead, e.g., `my_score`).
2. Cannot start with a number (e.g., `1player` will cause an Error; use `player1`).
3. Cannot use reserved keywords (e.g., `int`, `return`, `main`).

To use `printf` to display a variable's value, we must use the correct Format Specifier matching its data type:
- `int` uses `%d`
- `float` uses `%f`
- `char` uses `%c`

```c
#include <stdio.h>

int main() {
    int score = 100;
    float gpa = 3.99;
    char grade = 'A';

    printf("Score: %d\n", score);
    printf("GPA: %.2f\n", gpa); // %.2f means display 2 decimal places
    printf("Grade: %c\n", grade);
    return 0;
}
```

---

## Mathematical Calculations
C supports basic mathematical operators:
- Addition `+`
- Subtraction `-`
- Multiplication `*` 
- Division `/`
- Modulus `%` (Finds the remainder, popular for checking odd/even numbers)

> **Warning:** Dividing an integer by an integer (`int` / `int`) will **always truncate the decimal**. For example, `5 / 2` will result in `2` (not 2.5). If you want a decimal result, at least one of the values must be a `float`.

**Best Practice:** When calculating, we should store the computed value in a new variable first, and then display the new variable. This keeps the code clean and readable.

```c
#include <stdio.h>

int main() {
    int a = 10;
    int b = 3;
    
    // Calculate and store the results in new variables
    int sum = a + b;
    int difference = a - b;
    int quotient = a / b;
    int remainder = a % b;
    
    printf("10 + 3 = %d\n", sum);
    printf("10 - 3 = %d\n", difference);
    printf("10 / 3 = %d (Integer division truncates the decimal)\n", quotient);
    printf("10 %% 3 = %d (Used to find the remainder of division)\n", remainder); // Type %% to display the % sign
    return 0;
}
```

### Exercise 2.1: Multiplication Calculator
Receive 2 numbers (using `scanf`), calculate their product, store it in a new variable, and output the result.

```text
Enter number 1: 5
Enter number 2: 4
Result: 20
```

### Exercise 2.2: Rectangle Area
Receive a width and a length, store them in floating-point variables. Calculate the area (width x length) and output the result.

### Exercise 2.3: Cashier Change
Suppose a product costs 35 THB and the user pays with a 100 THB bill. Write a program to calculate the change, store it in a variable, and display the change amount.
