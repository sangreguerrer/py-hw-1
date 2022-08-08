class Student:
    def __init__(self,name,surname,gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.course_in_progress = []
        self.finished_course = []
        self.grades = {}
        def avg(m1,m2,m3,m4,m5,m6):
                for grade in self.grades:
                    average = float((sum(self.grades))/(len(self.grades)))
                    return average
        some_student = Student('Rouy','Eman',9.9,'Python,Git', 'Введение в программирование')
        def __str__(some_student):
            print(f"Имя: {self.name}, Фамилия: {self.surname},Средняя оценка за дз: {self.avg},Курсы в процессе изучения:{self.course_in_process},Завершённые курсы: {self.finished.course},sep = '\n")

    def rate_lec(self,name,surname,course,grade):
        if name and surname in Lecturer:
            if course in self.course_in_progress and self.finished_course:
                self.grades += {course:grade}
        else: 
            return 'Ошибка'

class Mentor:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        self.course_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = {}
        some_lecturer = Lecturer('Some','Buddy',9.9)
        def avg(m1,m2,m3,m4,m5,m6):
                for grade in self.grades:
                    average = float((sum(self.grades))/(len(self.grades)))
                    return average
        def __str__(some_lecturer):
            return f"Имя: {self.name}, Фамилия: {self.surname},Средняя оценка за лекции: {self.avg},sep = '\n'")
class Reviewer(Mentor):
    def rate_hw(self,student,course,grade):
        if isinstance(student,Student) and course in self.course_attached and course in student.course_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    some_reviewer = ('Some','Buddy')
    def __str__(some_reviewer):
            print(f"Имя: {self.name}, Фамилия: {self.surname}sep = '\n'")

