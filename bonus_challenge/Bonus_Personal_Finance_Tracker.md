# 🏆 Bonus Challenge: Personal Finance Tracker (ระบบจัดการรายรับ-รายจ่ายส่วนตัว)

---

## 🇹🇭 ภาษาไทย (Thai Version)

### 📌 คำอธิบายโจทย์
ยินดีด้วยที่เดินทางมาถึงโจทย์ข้อสุดท้ายของค่ายนี้! ในโจทย์นี้ เราจะมาสร้าง "ระบบจัดการรายรับ-รายจ่ายส่วนตัว" ซึ่งจะรวบรวมความรู้ทุกอย่างที่คุณได้เรียนมา (ตัวแปร, if-else, ลูป, Array และ ฟังก์ชัน) 

ให้คุณเขียนโปรแกรมที่จำลองการบันทึกรายจ่ายในชีวิตประจำวัน โดยระบบจะต้องให้ผู้ใช้ตั้งงบประมาณ (Budget) ตอนเริ่มต้น จากนั้นจะมีเมนูให้ผู้ใช้สามารถเพิ่มรายจ่าย ดูสรุปรายจ่าย หรือเช็คยอดเงินคงเหลือได้เรื่อยๆ จนกว่าจะกดออกจากโปรแกรม

### ✨ ฟีเจอร์ที่ต้องมี (Features Required)
1. **กำหนดงบประมาณ (Set Budget):** เมื่อเริ่มโปรแกรม ให้ผู้ใช้กรอกจำนวนเงินตั้งต้น
2. **เมนูหลัก (Main Menu):** โปรแกรมต้องแสดงเมนูให้ผู้ใช้เลือกทำรายการ (ใช้ `while` loop)
3. **เพิ่มรายจ่าย (Add Expense):** 
   - ให้ผู้ใช้เลือกหมวดหมู่ (1=อาหาร, 2=เดินทาง, 3=อื่นๆ)
   - กรอกจำนวนเงินที่จ่าย
   - *เงื่อนไขพิเศษ:* ถ้าจำนวนเงินที่กรอก มากกว่าเงินคงเหลือ ให้แสดงข้อความเตือนและไม่หักเงิน
4. **ดูสรุป (View Summary):** แสดงรายการรายจ่ายทั้งหมดที่บันทึกไว้ พร้อมบอกยอดรวม
5. **ดูยอดคงเหลือ (Check Balance):** แสดงยอดเงินคงเหลือปัจจุบัน

### 💡 คำใบ้ (Hints)
- ใช้ Array 2 ตัว: ตัวหนึ่งเก็บ "จำนวนเงิน" (เช่น `int amounts[20];`) และอีกตัวเก็บ "หมวดหมู่" (เช่น `int categories[20];`)
- สร้างตัวแปรมา 1 ตัว (เช่น `int count = 0;`) เพื่อนับว่าตอนนี้มีการบันทึกรายจ่ายไปแล้วกี่รายการ
- ลองแยกการทำงานเป็นฟังก์ชัน เช่น ฟังก์ชันสำหรับเพิ่มรายจ่าย และฟังก์ชันสำหรับแสดงสรุป

---

## 🇬🇧 English Version

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

## 💻 ตัวอย่างหน้าจอการทำงาน (Sample Output)

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
