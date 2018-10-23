class student:
    def __init__(self):
        self.student_idno=int(input('enter student id no'))
        self.student_name=input('enter the student name')
    def show(self):
        print('student idno:',self.student_idno)
        print('student name:',self.student_name)
