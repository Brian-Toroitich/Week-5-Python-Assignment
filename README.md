# Week-5-Python-Assignment
Week 5 Python Assignment
# 🎓 Students & Lecturers OOP Assignment

This project demonstrates **Object-Oriented Programming (OOP)** concepts in Python using the example of **Students and Lecturers** in a university environment.  
It covers **Classes, Objects, Encapsulation, Inheritance, and Polymorphism**.

---

## 📘 Assignment 1: Design Your Own Class

I created a base class `Person` and derived classes `Student` and `Lecturer`.

### Features:
- **Encapsulation:** The `__email` attribute is private and accessed through `get_email()`.
- **Inheritance:** `Student` and `Lecturer` inherit from `Person`.
- **Polymorphism:** Both `Student` and `Lecturer` override the `introduce()` method with their own version.
- **Methods:**
  - `Student.study()` → represents a student studying a subject.
  - `Lecturer.teach()` → represents a lecturer teaching a subject.

### Example:
```python
student1 = Student("Alice", 20, "alice@student.edu", "S123", "Computer Science")
lecturer1 = Lecturer("John", 45, "john@university.edu", "L456", "Computer Science")

student1.introduce()   # Polymorphism
student1.study("Data Structures")

lecturer1.introduce()  # Polymorphism
lecturer1.teach("Artificial Intelligence")
