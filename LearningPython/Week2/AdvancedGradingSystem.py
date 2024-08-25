class GradingStudent:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def student_info(self):
        return f"{self.name} of age {self.age} has scored {self.marks} and the grade obtained is: "

    def display_grade(self):
        if 90 < self.marks < 100:
            return "A"
        elif 79 < self.marks < 89:
            return "B"
        elif 69 < self.marks < 79:
            return "C"
        elif 59 < self.marks < 69:
            return "D"
        else:
            return "Fail"

name = input("Enter your name: ")
age = int(input("Enter your age: "))
marksObtained = int(input("Enter marks obtained: "))

student = GradingStudent(name, age, marksObtained)
print(student.student_info())
print(student.display_grade())