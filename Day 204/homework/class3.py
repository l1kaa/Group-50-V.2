# 3) შექმენი კლასი ExamResult: რომელსაც ექნება student_name, math, english, science. შექმენი 2 სტუდენტი და დაბეჭდე: ვის აქვს ჯამური ქულა მეტი.

class ExamResult:
# 3) შექმენი კლასი ExamResult: რომელსაც ექნება student_name, math, english, science. შექმენი 2 სტუდენტი და დაბეჭდე: ვის აქვს ჯამური ქულა მეტი.
    def __init__(self, student_name, math, english, science):
        self.name = student_name
        self.math = math
        self.english = english
        self.science = science

    def calculate_sum(self):
        sumn = 0
        sumn += self.math 
        sumn += self.english
        sumn += self.science
        return sumn



student1 = ExamResult('Lika', 100, 100, 100)
student2 = ExamResult('Saba', 78, 50, 19)

sum1 = student1.calculate_sum()
sum2 = student2.calculate_sum()


print(f'{student1.name} has a greater score ({sum1}) than {student2.name} ({sum2})' if sum1 > sum2 else f'{student2.name} has a greater score ({sum2}) than {student1.name} ({sum1})')