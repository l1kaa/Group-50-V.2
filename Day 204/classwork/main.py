# 1) შექმენი კლასი Student, რომელსაც ექნება:name,age,grade. init-ის გამოყენებით.შემდეგ: შექმენი 2 სტუდენტის ობიექტი და დაბეჭდე მათი მონაცემები

class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

student1 = Student('Lika', 18, 'Female')
student2 = Student('Nika', 20, 'Male')

print(student1.name)
print(student1.age)
print(student1.gender)

print(student2.name)
print(student2.age)
print(student2.gender)