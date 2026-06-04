# Module 4: Arrays and Functions

## Arrays
If we want to store the exam scores of 50 students, creating 50 separate variables would not be an efficient approach. We can use an **Array** to store multiple values of the same data type under a single variable name. The position of each piece of data is specified by its "Index number".

> **Crucial Note:** Array Index numbers **always start at 0** (the first piece of data is at Index 0).

```c
#include <stdio.h>

int main() {
    // Create an Array named 'scores' to hold 5 'int' values
    int scores[5] = {10, 20, 30, 40, 50};
    
    printf("Score of person 1 (Index 0): %d\n", scores[0]);
    printf("Score of person 5 (Index 4): %d\n", scores[4]);
    
    // We commonly use a For Loop with Arrays to access every element
    for(int i = 0; i < 5; i++) {
        printf("Score of person %d: %d\n", i+1, scores[i]);
    }
    return 0;
}
```

### Creating Strings using Arrays of Chars
In C, there is no direct `String` variable type. However, we can use an Array of `char` (which normally holds only 1 character) to store a sequence of characters, creating a long text string.

```c
#include <stdio.h>

int main() {
    // Reserve 20 slots to hold text (including spaces and the special \0 null-terminator that ends the String)
    char name[20]; 
    
    printf("Enter your name: ");
    // Receiving a String with scanf does NOT require an & before the variable name
    scanf("%s", name); 
    
    // To display a String, we use %s
    printf("Welcome, %s!\n", name);
    return 0;
}
```

### Exercise 4.1: Cash Register Total
Receive the prices of 5 items and store them in an Array. Then, use a For Loop to add all the numbers together and display the total sum.

### Exercise 4.2: Find the Average
Building on Exercise 4.1, use the total sum to calculate the average. (Hint: Be careful with data types when dividing to ensure you get a decimal result).

---

## Functions
As programs grow larger, writing all commands inside `main` makes the code complex and messy. We separate parts of the code into **functions** to keep things organized and to make the code reusable.

```c
#include <stdio.h>

// 1. "Non-returning" function (specify the type as void)
// Used when you want the function to perform a task without sending a value back.
void say_hello() {
    printf("Hello CBC!\n");
}

// 2. "Returning" function (specify a data type, e.g., int)
// Used when you want the function to calculate something and send the result back to the main program to be used.
int add(int a, int b) {
    int result = a + b;
    return result; // Return the result back
}

int main() {
    say_hello(); // Call the say_hello function
    
    // Call the add function by passing the values 5 and 7
    // and create a 'sum' variable to receive the value returned by the function
    int sum = add(5, 7); 
    
    printf("5 + 7 = %d\n", sum);
    
    return 0;
}
```

### Exercise 4.3: Double It! Function
Create a function named `double_number` that receives 1 number (int). Multiply it by 2, and then return the value to be displayed inside `main`.

### Exercise 4.4: Pass/Fail Checker Function
Create a function named `check_pass` that receives 1 score (int).
- If score >= 50, return 1 (meaning Pass)
- If score < 50, return 0 (meaning Fail)
Then, inside `main`, call the function and display the result.
