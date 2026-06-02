import nbformat as nbf

def create_nb():
    nb = nbf.v4.new_notebook()
    # กำหนด Metadata ให้ Notebook รู้ว่านี่คือ C Kernel
    nb.metadata = {
        "kernelspec": {
            "display_name": "C",
            "language": "c",
            "name": "c"
        }
    }
    return nb

def add_md(nb, text):
    nb.cells.append(nbf.v4.new_markdown_cell(text))

def add_code(nb, code):
    nb.cells.append(nbf.v4.new_code_cell(code))

# --- Notebook 1: Fundamentals ---
nb1 = create_nb()
add_md(nb1, "# 🚀 ยินดีต้อนรับสู่ C Beginner! (CBC Boost Camp)\n\nสวัสดีครับน้องๆ! วันนี้เราจะมาเรียนรู้ภาษา C กันแบบชิลๆ 💻\n\n## 📝 โครงสร้างพื้นฐานของภาษา C\nภาษา C จะมีโครงสร้างหลักๆ ที่ขาดไม่ได้เลยคือ `main function` ครับ โค้ดทุกอย่างจะเริ่มทำงานจากตรงนี้แหละ!")
add_code(nb1, "#include <stdio.h> // โหลดเครื่องมือพื้นฐาน (Header)\n\nint main() {\n    // โค้ดของเราจะอยู่ในนี้!\n    return 0; // จบโปรแกรมแบบสวยงาม\n}")
add_md(nb1, "## 🖨️ การแสดงผลด้วย `printf`\nอยากให้คอมพิวเตอร์พูดอะไร ใช้คำสั่ง `printf` ได้เลย!")
add_code(nb1, "#include <stdio.h>\n\nint main() {\n    printf(\"Hello CBC Boost Camp!\\n\");\n    printf(\"My name is ...\\n\");\n    return 0;\n}")
add_md(nb1, "### 🎯 แบบฝึกหัด 1.1\nลองเปลี่ยนคำว่า `My name is ...` เป็นชื่อของน้องๆ ในโค้ดข้างบนดูสิครับ แล้วกดรันใหม่เลย!")

add_md(nb1, "---\n## 📥 การรับค่าด้วย `scanf`\nเวลาเราอยากให้ผู้ใช้พิมพ์ข้อมูลเข้ามา เราจะใช้ `scanf` ครับ อย่าลืมใส่ `&` หน้าชื่อตัวแปรด้วยนะ (ยกเว้นตัวแปรประเภทข้อความ)")
add_code(nb1, "#include <stdio.h>\n\nint main() {\n    int age;\n    printf(\"How old are you?: \");\n    scanf(\"%d\", &age); // รอรับตัวเลข int\n    printf(\"Wow, you are %d years old!\\n\", age);\n    return 0;\n}")
add_md(nb1, "### 🎯 แบบฝึกหัด 1.2\nลองเขียนโค้ดรับ **ปีเกิด (ค.ศ.)** แล้วคำนวณอายุออกมาดูสิ! (ใบ้ให้: เอา 2026 - ปีเกิด)")

# --- Notebook 2: Data Types ---
nb2 = create_nb()
add_md(nb2, "# 📦 ชนิดข้อมูล (Data Types) และ ตัวแปร (Variables)\n\nตัวแปรก็เหมือน 'กล่อง' ที่เอาไว้เก็บข้อมูลครับ ซึ่งกล่องแต่ละใบก็เก็บของได้ต่างชนิดกัน\n\n- `int` เก็บจำนวนเต็ม (เช่น 5, -10)\n- `float` หรือ `double` เก็บทศนิยม (เช่น 3.14)\n- `char` เก็บตัวอักษร 1 ตัว (เช่น 'A')\n\nเวลา `printf` เราต้องใช้ 'รูปแบบ' (Format) ให้ตรงด้วยนะ:\n- `%d` สำหรับ int\n- `%f` สำหรับ float\n- `%c` สำหรับ char")
add_code(nb2, "#include <stdio.h>\n\nint main() {\n    int score = 100;\n    float gpa = 3.99;\n    char grade = 'A';\n\n    printf(\"Score: %d\\n\", score);\n    printf(\"GPA: %.2f\\n\", gpa); // %.2f คือเอาทศนิยมแค่ 2 ตำแหน่ง\n    printf(\"Grade: %c\\n\", grade);\n    return 0;\n}")

add_md(nb2, "---\n## 🧮 การคำนวณทางคณิตศาสตร์\nบวก `+`, ลบ `-`, คูณ `*`, หาร `/`, และ หารเอาเศษ `%` (Modulus)\n\n> ⚠️ **ระวัง!** การหารเลขจำนวนเต็ม (int / int) จะปัดเศษทิ้งเสมอ! ถ้าอยากได้ทศนิยม ต้องมีตัวใดตัวหนึ่งเป็น float")
add_code(nb2, "#include <stdio.h>\n\nint main() {\n    int a = 10;\n    int b = 3;\n    \n    printf(\"10 + 3 = %d\\n\", a + b);\n    printf(\"10 - 3 = %d\\n\", a - b);\n    printf(\"10 / 3 = %d (อ้าว เศษหายไปไหน?)\\n\", a / b);\n    printf(\"10 %% 3 = %d (อยู่นี่ไงเศษ!)\\n\", a %% b);\n    return 0;\n}")

add_md(nb2, "### 🎯 แบบฝึกหัด 2.1\nรับค่าตัวเลข 2 ตัว (ใช้ `scanf` สองรอบ หรือรับทีเดียว `%d %d` ก็ได้) จากนั้นให้โปรแกรมแสดงผลการ **คูณ** ของสองตัวนี้")
add_code(nb2, "#include <stdio.h>\n\nint main() {\n    // เขียนโค้ดตรงนี้เลย!\n    printf(\"ป้อนตัวเลข 2 ตัว: \");\n    \n    return 0;\n}")

# --- Notebook 3: Flow Control ---
nb3 = create_nb()
add_md(nb3, "# 🚦 การควบคุมทิศทางโปรแกรม (Flow Control)\n\nบางครั้งเราอยากให้โปรแกรม 'ตัดสินใจ' หรือ 'ทำซ้ำ' เรามาดูกันว่าทำยังไง!\n\n## 🧐 เงื่อนไข if - else if - else\nถ้า (if) เงื่อนไขเป็นจริง ให้ทำสิ่งนี้, ไม่งั้นถ้า (else if)..., ไม่งั้น (else)...")
add_code(nb3, "#include <stdio.h>\n\nint main() {\n    int money = 50;\n    \n    if (money >= 100) {\n        printf(\"กินชาบู! 🍲\\n\");\n    } else if (money >= 50) {\n        printf(\"กินกะเพรา 🍛\\n\");\n    } else {\n        printf(\"กินมาม่า 🍜\\n\");\n    }\n    return 0;\n}")

add_md(nb3, "### 🎯 แบบฝึกหัด 3.1: เครื่องตัดเกรด\nรับค่าคะแนน 1 ตัว (int)\n- >= 80 ได้ A\n- >= 70 ได้ B\n- >= 60 ได้ C\n- >= 50 ได้ D\n- < 50 ได้ F\n- แฮกเกอร์: ถ้าคะแนน > 100 ให้ปรินต์ 'Cheating'")
add_code(nb3, "#include <stdio.h>\n\nint main() {\n    // ลองเขียนโปรแกรมตัดเกรดที่นี่!\n    \n    return 0;\n}")

add_md(nb3, "---\n## 🔄 การทำซ้ำ (Loops)\nขี้เกียจพิมพ์ `printf` ซ้ำๆ หรอ? ใช้ Loop สิ!\n\n### While Loop (ทำไปเรื่อยๆ ตราบใดที่เงื่อนไขเป็นจริง)")
add_code(nb3, "#include <stdio.h>\n\nint main() {\n    int i = 0;\n    while (i < 5) {\n        printf(\"%d\\n\", i);\n        i++; // อย่าลืมเพิ่มค่า i ไม่งั้นลูปอินฟินิตี้ เครื่องค้างนะ!\n    }\n    return 0;\n}")

add_md(nb3, "### For Loop (รู้จำนวนรอบที่ชัดเจน)")
add_code(nb3, "#include <stdio.h>\n\nint main() {\n    // for (เริ่มต้น ; เงื่อนไข ; การเปลี่ยนแปลง)\n    for (int i = 5; i > 0; i--) {\n        printf(\"เหลือเวลา %d วินาที\\n\", i);\n    }\n    printf(\"ตู้ม! 💥\\n\");\n    return 0;\n}")

add_md(nb3, "### 🎯 แบบฝึกหัด 3.2: ลูปสูตรคูณ\nรับค่าแม่สูตรคูณ 1 ตัว แล้วปรินต์สูตรคูณแม่นั้นตั้งแต่ x1 ถึง x12")
add_code(nb3, "#include <stdio.h>\n\nint main() {\n    // เขียนสูตรคูณตรงนี้เลย!\n    \n    return 0;\n}")


# --- Notebook 4: Arrays & Functions ---
nb4 = create_nb()
add_md(nb4, "# 📚 อาร์เรย์ (Arrays) และ ฟังก์ชัน (Functions)\n\n## 📦 Arrays (กล่องใส่ของหลายชิ้น)\nเมื่อเราอยากเก็บข้อมูลประเภทเดียวกันหลายๆ ตัว เราใช้ Array (จำไว้นะ! หมายเลขช่องเริ่มจาก 0 เสมอ)")
add_code(nb4, "#include <stdio.h>\n\nint main() {\n    int scores[5] = {10, 20, 30, 40, 50};\n    \n    printf(\"คะแนนคนที่ 1 (ช่องที่ 0): %d\\n\", scores[0]);\n    \n    // ใช้ for loop วนปรินต์ทุกตัวสบายมาก\n    for(int i = 0; i < 5; i++) {\n        printf(\"คะแนนคนที่ %d: %d\\n\", i+1, scores[i]);\n    }\n    return 0;\n}")

add_md(nb4, "### 🎯 แบบฝึกหัด 4.1: หาค่าเฉลี่ย\nรับคะแนนสอบ 5 ตัวเก็บลง Array แล้วหา 'ค่าเฉลี่ย' ออกมา (ผลรวม / 5.0)")
add_code(nb4, "#include <stdio.h>\n\nint main() {\n    // ลองคำนวณค่าเฉลี่ยดูครับ\n    \n    return 0;\n}")

add_md(nb4, "---\n## 🛠️ ฟังก์ชัน (Functions)\nแยกโค้ดเป็นส่วนย่อยๆ ให้เรียกใช้ง่ายขึ้น เป็นระเบียบขึ้น และนำกลับมาใช้ใหม่ได้")
add_code(nb4, "#include <stdio.h>\n\n// สร้างฟังก์ชันชื่อ say_hello (ทำหน้าที่อย่างเดียว ไม่คืนค่า กลับมาให้เรา)\nvoid say_hello() {\n    printf(\"Hello CBC! 👋\\n\");\n}\n\n// ฟังก์ชันรับเลข 2 ตัว คืนค่าผลบวก (คืนค่าเป็น int)\nint add(int a, int b) {\n    return a + b;\n}\n\nint main() {\n    say_hello();\n    say_hello();\n    \n    int sum = add(5, 7);\n    printf(\"5 + 7 = %d\\n\", sum);\n    return 0;\n}")

add_md(nb4, "### 🎯 แบบฝึกหัด 4.2: ฟังก์ชันเช็คเลขคู่/คี่\nสร้างฟังก์ชันที่รับค่าตัวเลข (int) แล้ว return 1 ถ้าเป็นเลขคู่ และ return 0 ถ้าเป็นเลขคี่ จากนั้นลองเรียกใช้ใน main ดูนะ")
add_code(nb4, "#include <stdio.h>\n\n// สร้างฟังก์ชันตรงนี้\n\nint main() {\n    // ลองเรียกใช้ฟังก์ชันตรงนี้\n    \n    return 0;\n}")

import json
with open('01_C_Fundamentals.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb1, f)
with open('02_C_Data_Types.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb2, f)
with open('03_C_Flow_Control.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb3, f)
with open('04_Arrays_and_Functions.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb4, f)
print("Notebooks updated to use Pure C Kernel successfully!")
