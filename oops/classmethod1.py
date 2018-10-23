#claas method with static variables and methods

class student:
    stu_name="prasad"
    stu_cno=902766763
    @staticmethod
    def display():
        print('i am the static method')
    @classmethod
    def show(cls):
        print('i am the class method')
        print(cls.stu_name)
        print(cls.stu_cno)
        cls.display()
student.show()