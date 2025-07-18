# 👋 Smart Greeting App (Python Mini Project)

> **“Ghar jaisa welcome, ab code bhi karega – Good Morning se Good Night tak, time ke hisaab se!”**  
> This is a smart and beginner-friendly Python project that greets the user based on real-time system clock – perfect for students, learners, and mini project presentations. 🧠

---

## 📌 About the Project

Smart Greeting App ek chhoti si Python script hai jo real-time clock ka use karke user ko greet karti hai based on current hour of the day.

Yeh app:
- Python ka `time` module use karta hai 🕒
- User se naam input leta hai 🧑
- `if-elif-else` conditions ka use karke smart greeting deta hai 🌞🌆🌙

---

## 🔁 How It Works

### Input:
- User ka naam (`input()` se)

### Logic:
- System time se current hour (`time.strftime("%H")`) nikaala jata hai
- Hour ke basis par greeting decide hoti hai:

| Time (24-Hour)     | Greeting          |
|--------------------|-------------------|
| 04:00 - 11:59      | Good Morning ☀️   |
| 12:00 - 16:59      | Good Afternoon 😎 |
| 17:00 - 20:59      | Good Evening 🌇   |
| 21:00 - 03:59      | Good Night 🌙     |

---

## 👨‍💻 Code Example

```python
import time

name = input("Enter your name: ").capitalize()
present_time = int(time.strftime("%H"))

if 4 <= present_time < 12:
    print(f"Good Morning {name}")
elif 12 <= present_time < 17:
    print(f"Good Afternoon {name}")
elif 17 <= present_time < 21:
    print(f"Good Evening {name}")
else:
    print(f"Good Night {name}")

print("Thank you Sir!")
