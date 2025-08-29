
class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.__email = email  # private attribute (encapsulation)

    def introduce(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old.")

    def get_email(self):
        return self.__email


# Derived class: Student
class Student(Person):
    def __init__(self, name, age, email, student_id, course):
        super().__init__(name, age, email)
        self.student_id = student_id
        self.course = course

    def introduce(self):  # Polymorphism (overriding)
        print(f"I am {self.name}, a student taking {self.course}.")

    def study(self, subject):
        print(f"{self.name} is studying {subject}.")


# Derived class: Lecturer
class Lecturer(Person):
    def __init__(self, name, age, email, staff_id, department):
        super().__init__(name, age, email)
        self.staff_id = staff_id
        self.department = department

    def introduce(self):  # Polymorphism (overriding)
        print(f"I am Dr. {self.name}, a lecturer in the {self.department} department.")

    def teach(self, subject):
        print(f"Dr. {self.name} is teaching {subject}.")


# Creating objects
student1 = Student("Brian", 20, "brian@plpacademy.africa", "S123", "Python Programming")
lecturer1 = Lecturer("Chakin", 45, "chakin@plpacademy.africa", "L456", "Python Programming")

# Demonstration
student1.introduce()
student1.study("Object-Oriented Programming")
print("Student email :", student1.get_email())

lecturer1.introduce()
lecturer1.teach("Object-Oriented Programming")
print("Lecturer email :", lecturer1.get_email())
