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


---

# Module 3: Flow Control

Normally, a program executes sequentially from top to bottom. However, we can control the flow to let the program "make decisions" or "repeat" tasks.

## Conditionals: if - else if - else
Used to check conditions. If the condition is true (True), the program will execute the code block inside the braces.

Comparison operators:
- `==` Equal to
- `!=` Not equal to
- `>` Greater than
- `<` Less than
- `>=` Greater than or equal to
- `<=` Less than or equal to

```c
#include <stdio.h>

int main() {
    int money = 50;
    
    // The program checks from top to bottom. Once a true condition is met, it executes and exits the if-block immediately.
    if (money >= 100) {
        printf("Eat Shabu\n");
    } else if (money >= 50) {
        printf("Eat Basil Chicken (Krapow)\n");
    } else {
        printf("Eat Instant Noodles (Mama)\n");
    }
    return 0;
}
```

### Exercise 3.1: Grade Calculator
Receive 1 score (int)
- If score >= 80, get Grade A
- If score >= 70, get Grade B
- If score >= 60, get Grade C
- If score >= 50, get Grade D
- If score < 50, get Grade F
*Special Condition:* If the entered score is over 100, display the message 'Cheating!'

### Exercise 3.2: Even or Odd Checker
Receive 1 number and tell whether it is "Even" or "Odd".
*(Hint: An even number is a number that, when divided by 2, leaves a remainder of 0. You can use the `%` operator to check this).*

---

## Loops
Used to command the program to repeat the same block of code based on a specified condition.

### While Loop (Repeat as long as the condition is true)
Ideal for situations where we don't know the exact number of iterations.

```c
#include <stdio.h>

int main() {
    int i = 0; // Define the starting point
    
    while (i < 5) { // Check the condition
        printf("%d\n", i);
        i++; // IMPORTANT: You must always update the value, otherwise the loop will never end (Infinity Loop)
    }
    return 0;
}
```

### For Loop (Repeat a specific number of times)
Consolidates the starting point, condition check, and value update into a single line.

```c
#include <stdio.h>

int main() {
    // for (start ; condition check ; update)
    for (int i = 5; i > 0; i--) {
        printf("%d seconds remaining\n", i);
    }
    printf("Time's up!\n");
    return 0;
}
```

### Exercise 3.3: Multiplication Table Program
Receive a base multiplier (1 number) and use a Loop to print the multiplication table for that number from 1 to 12.
Example:
```text
Enter number: 2
2 x 1 = 2
2 x 2 = 4
...
2 x 12 = 24
```

### Exercise 3.4: Print Stars
Receive 1 number `N` and use a Loop to print the `*` symbol `N` times in a row.
(For example, if the user inputs 5, the output should be `*****`)
