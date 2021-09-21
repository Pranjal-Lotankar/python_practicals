'''Design a class that store the information of student and display the same'''
class Student:

    def init(self, name, sex, course, result):
        self.name = name
        self.sex = sex
        self.course = course
        self.result = result

    def display(self, name, sex, course, result):
        self.name = name
        self.sex = sex
        self.course = course
        self.result = result
        print('Name:', name)
        print('Sex:', sex)
        print('course:', course)
        print('result:', result)

s1=Student()
s1.display('Pranjal', 'F', 'IT', 81)
