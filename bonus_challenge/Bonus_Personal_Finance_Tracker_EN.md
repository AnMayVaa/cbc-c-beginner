# 🏆 Bonus Challenge: Personal Finance Tracker

### 📌 Problem Description
Congratulations on reaching the final challenge of the camp! In this task, you will build a "Personal Finance Tracker". This will combine everything you have learned today (Variables, if-else, Loops, Arrays, and Functions).

Write a program that simulates a daily expense tracker. The system must ask the user to set an initial budget. Then, it should display a menu allowing the user to add expenses, view a summary, or check their remaining balance continuously until they choose to exit.

### ✨ Features Required
1. **Set Budget:** Ask the user to input their starting budget when the program starts.
2. **Main Menu:** Display a menu of options for the user to choose from (use a `while` loop).
3. **Add Expense:** 
   - Ask the user to select a category (1=Food, 2=Transport, 3=Other).
   - Ask for the expense amount.
   - *Special Condition:* If the amount is greater than the remaining balance, print a warning message and do not deduct the money.
4. **View Summary:** Display all recorded expenses and the total amount spent.
5. **Check Balance:** Display the current remaining balance.

### 💡 Hints
- Use 2 Arrays: One to store "amounts" (e.g., `int amounts[20];`) and another to store "categories" (e.g., `int categories[20];`).
- Create a variable (e.g., `int count = 0;`) to keep track of how many expenses have been recorded so far.
- Try breaking down the program into functions, such as one function for adding an expense and another for viewing the summary.

---

## 💻 Sample Output

```text
Enter your budget: 500

=== Personal Finance Tracker ===
1. Add Expense
2. View Summary
3. Check Balance
0. Exit
Select: 1

Category (1=Food, 2=Transport, 3=Other): 1
Amount: 120
Expense added!

Select: 1
Category (1=Food, 2=Transport, 3=Other): 2
Amount: 45
Expense added!

Select: 2
--- Expense Summary ---
#1 [Food]      120 Baht
#2 [Transport]  45 Baht
Total Expenses: 165 Baht

Select: 3
Remaining Balance: 335 Baht

Select: 0
Goodbye!
```
