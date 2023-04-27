''' student class'''
# Imports
import random


class Student():
    '''Create parent class Student with 2 attributes and 2 methods'''

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def bday(self):
        '''birthday'''
        self.age += 1
        return self.age

    def advance_grade(self):
        '''move up a grade'''
        self.grade += 1
        return self.grade


class BloomTechStudent(Student):
    '''bloomtech student class'''

    def __init__(self, name, age, grade, enroll_status=True):
        super().__init__(name, age, grade)
        self.enroll_status = enroll_status

    def change_status(self):
        '''change enroll status'''
        if self.enroll_status:
            self.enroll_status = False
            return 'Please re-enroll'
        self.enroll_status = True
        return 'Currently enrolled!'

    def __repr__(self) -> str:
        greetings =  f'Hello {self.age} year old {self.name}'
        greeting2 = f'in grade {self.grade} with an enrollment status as {self.enroll_status}'
        return greetings + greeting2

def student_generator(class_size=30):
    '''student_generator that generates random values
    for bloomtech student attributes'''
    names = ['Alan', 'Ben', 'Cameron', 'Dave', 'Earl']

    ran_name = random.choice(names)

    age = random.randint(0, 100)

    grade = random.randint(0, 13)

    enroll_status = random.choice(['True', 'False'])

    students = []

    for _ in range(class_size):
        students.append(BloomTechStudent(
            ran_name, age, grade, enroll_status))

    return students


student_list = student_generator(2)

print(student_list)
