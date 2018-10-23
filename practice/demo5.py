class electricity():
    price=0
    def calculate(self):
        self.no_of_units=int(input('enter no of units'))
        if self.no_of_units<=150:
            pass
        elif self.no_of_units>150 and self.no_of_units<=300:
            price=self.no_of_units*5.46
            print('price:',price)
        else:
            price=self.no_of_units*9.86
            print('price',price)
e1=electricity()
e1.calculate()