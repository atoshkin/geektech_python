class Person:
    def init(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self, full_name, age, is_married):
        print(f"fullname: {full_name} \n age: {age} \n is_married: {is_married}")

    def output(self,):
        return f"full name {self.full_name}\n" \
               f"age {self.age}\n" \
               f"is married {self.is_married}\n" \



class Student(Person):
    def __init__(self, full_name, age, is_married, marks):
        Person.init(self, full_name, age, is_married)
        self.marks = marks

    def fair(self):
        print(sum(self.marks) / 5)

class Teacher(Person):
    salary = 12000

    def __init__(self, full_name, age, is_married, experience=3):
        Person.init(self, full_name, age, is_married)
        self.experience = experience

    def Salary(self):
        if self.experience > 3:
            teacher_salary = self.salary + ((self.salary/100*5) * (self.experience-3))
            return teacher_salary

Sensei = Teacher("Sensei", 26, False, 5,)

print(f'{Sensei.full_name} {Sensei.age} {Sensei.is_married} {Sensei.experience}\nSensei money: {Sensei.Salary()}')


def create_students():
    student1 = Student(full_name="Atosh", age=14, is_married=False, marks={
        "математика":77,
        "биология": 55,
        "история": 44,
        "физика": 88,
        "англ-язык": 99,
    })
    student2 = Student(full_name="Matosh", age=15, is_married=False, marks={
        "математика": 100,
        "биология": 74,
        "история": 51,
        "физика": 57,
        "англ-язык": 44,
    })
    student3 = Student(full_name="Pitosh", age=18, is_married=False, marks={
        "математика": 55,
        "биология": 51,
        "история": 19,
        "физика": 47,
        "англ-язык": 22,
    })

    rst = [student1, student2, student3]
    return rst

students = create_students()
for i in students:
    list = []
    for marks in i.marks.values():
        list.append(marks)
    print(f"Name: {i.full_name}\n"
          f"Age: {i.age}\n"
          f"Maried: {i.is_married}\n"
          f"Average marks: {sum(list)/len(list)}\n")