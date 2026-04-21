# 📚 Library Management System (CLI)

A simple Python-based command-line application to manage books in a library.  
This project demonstrates core programming concepts like dictionaries, functions, and date handling.

---

## 🚀 Features

- Add new books
- Issue books
- Return books
- Track issued books
- Calculate overdue fines based on return delay
- Custom return date input (for testing)

---

## 💰 Fine System

If a book is returned late, fines are applied as:

- 1st week → ₹10/day
- 2nd week → ₹20/day
- 3rd week → ₹60/day
- and so on...

---

## 🛠️ Tech Used

- Python
- `datetime` module
- Dictionary-based data storage

---

## ▶️ How to Run

```bash
python main.py