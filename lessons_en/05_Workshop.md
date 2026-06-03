# Module 5: C Programming Workshop

This section contains Workshop exercises that allow you to apply all the knowledge you've learned. Feel free to choose the problems that interest you!

---

## Part A: Applying the Fundamentals (Modules 1-3)

### 1. Mini Calculator
Write a program that receives 2 numbers and 1 mathematical operator (`+`, `-`, `*`, `/`), then calculates and displays the result.
> **Hint:** When using `scanf` to receive a single character, use `%c`. It is highly recommended to add a space before the format specifier, like `scanf(" %c", &op);`, to prevent issues with leftover Enter (newline) characters. Then, use `if-else if` to check the operator and calculate the result.

### 2. Vending Machine
Write a program to simulate a vending machine. Set predefined prices (e.g., Water 10 THB, Cola 15 THB). Ask the user to input the **amount of money inserted** and **select a menu item**.
- If the money is sufficient: Calculate and display the "Change".
- If the money is insufficient: Display "Insufficient funds, missing X THB".
> **Hint:** Create a menu for the user to choose from (1=Water, 2=Cola). Use `if-else` to check if `money inserted - drink price` is greater than or equal to 0.

### 3. Guess the Number
The program sets a secret number (e.g., 42). The user repeatedly guesses the number, and the program responds with "Too high" or "Too low" until they guess correctly.
> **Hint:** Use a `while` loop with the condition `guessed number != secret number`. Inside the loop, use `if-else` to check whether the user's input is greater or less than the secret number.

### 4. Star Pyramid
Receive 1 number `N`, then display a right-angled triangle made of `*` symbols with a height of `N` layers.
Example if $N=4$:
```text
*
**
***
****
```
> **Hint:** You need to use a Nested `for` Loop (2 layers). The outer loop controls the "line/row" and the inner loop controls the "number of stars". The number of stars on each line is equal to the current line number.

### 5. Find Maximum
Let the user input scores continuously. If the user types `-1`, the program stops and displays the "highest score" entered.
> **Hint:** Create a variable `max_score = 0` outside the loop. When inside the loop receiving a value, check if the entered value is greater than `max_score`. If it is, replace `max_score` with that new value.

---

## Part B: Advanced Application (Arrays and Functions)

### 6. Supermarket Cash Register
Receive the prices of 5 items and store them in an `Array`. Send that Array to a `Function` to calculate the total sum including Value Added Tax (VAT 7%) before returning the final amount to be displayed.
> **Hint:** Create a function that accepts an Array as a parameter (e.g., `float calc_total(int arr[])`). Use a loop to find the total sum, then `return` the total sum multiplied by 1.07.

### 7. Pass/Fail Finder
Given an `Array` containing the exam scores of 10 students, create a `Function` to count how many students passed (score >= 50) and how many failed.
> **Hint:** Inside the function, use a loop to check the data in the Array slot by slot. If score >= 50, increment a `pass_count` variable. If not, increment a `fail_count` variable.

### 8. Word Reverser
Receive a single word, then display that word printed backward (e.g., entering `hello` outputs `olleh`).
> **Hint:** You need to include the `<string.h>` library to use the `strlen()` function to find the length of the string. Then, use a `for` loop to print the characters backward from the last index down to 0.

### 9. Personal ATM
Create 3 functions: `deposit()`, `withdraw()`, and `check_balance()`. Allow the user to repeatedly perform these transactions switching back and forth via a menu until they choose to exit.
> **Hint:** Use a `while` loop to create the menu. Use a `balance` variable in `main` and pass it to the functions to calculate the new amount. Then have the functions `return` the value back to update the `balance` variable.

### 10. Lucky Draw System
Create a program that randomly selects a lucky winner from a list of 5 names stored in an Array.
> **Hint:** 
> 1. In C, we use the `<stdlib.h>` library for generating random numbers and `<time.h>` to access the current time.
> 2. Type the command `srand(time(NULL));` at the very top inside `main()` just once to initialize the random seed so it doesn't pick the same sequence every time.
> 3. Use the command `int random_index = rand() % 5;` to get a random number from 0 to 4.
> 4. Use `random_index` as the index slot to pull the lucky winner's name from the Array.
