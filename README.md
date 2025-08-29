# Week-5-Python-Assignment
Week 5 Python Assignment
# Students & Lecturers OOP Assignment

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



#Activity 2: Polymorphism Challenge – Vehicles

This project demonstrates the concept of **Polymorphism** in Object-Oriented Programming (OOP) using the example of **Vehicles**.  

---

## 📘 Overview
- A **base class** `Vehicle` is defined with a method `move()`.
- Different vehicle types (`Car`, `Plane`, `Boat`, `Bicycle`) inherit from `Vehicle`.
- Each subclass **overrides** the `move()` method to describe its unique movement:
  - `Car.move()` → Prints "🚗 Driving on the road."
  - `Plane.move()` → Prints "✈️ Flying in the sky."
  - `Boat.move()` → Prints "🚤 Sailing on water."
  - `Bicycle.move()` → Prints "🚴 Pedaling on the street."

This shows how the same method name can perform different actions depending on the object — a core idea of **polymorphism**.

---

## 🧩 Code Example

```python
# Base class
class Vehicle:
    def move(self):
        print("This vehicle can move in some way.")

# Subclasses overriding move()
class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road.")

class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky.")

class Boat(Vehicle):
    def move(self):
        print("🚤 Sailing on water.")

class Bicycle(Vehicle):
    def move(self):
        print("🚴 Pedaling on the street.")

# Demonstration
vehicles = [Car(), Plane(), Boat(), Bicycle()]

for v in vehicles:
    v.move()
