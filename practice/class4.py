class student:
    course_name = 'master of computer applications'
    college_name='s v university'
    college_code=1020033
    def details(self):
        self.id=int(input('enter id:'))
        self.name=input('enter student name:')
        self.gender=input('enter type of gender:')
        self.email=input('enter student mail:')
        self.contactnumber=input('enter student contact number:')
        self.mm=int(input('enter mm value:'))
        self.qa=int(input('enter qa value'))
        self.hra=int(input('enter hra value'))
        self.totalmarks=(self.mm+self.qa+self.hra)
    def display(self):
        print('studentname:',self.name)
        print('studentid:',self.id)
        print('gender:',self.gender)
        print('email:',self.email)
        print('contactnumber:',self.contactnumber)
        print('coursename:',student.course_name)
        print('collegename:',student.college_name)
        print('collegecode',student.college_code)
        print('marketing management:',self.mm)
        print('quantitative analasis:',self.qa)
        print('human resourse analysis:',self.hra)
        print('totalmarks:',self.totalmarks)
#calling block
stu=student()
stu.details()
stu.display()
stu1=student()
stu1.details()
stu1.display()







