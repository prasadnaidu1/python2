#class method
class employee:
    @classmethod
    def display(cls):
        print('i am the class method')
        print(cls)
employee.display()
