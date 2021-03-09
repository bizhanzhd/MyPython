class Calculator:

    def __init__(self):
        print("---------")
    def add(self,x,y):
        result=x+y
        print("---> ",result)
    def subtract(self,x,y):
        result=x-y
        print("---> ",result)
    def multiply(self,x,y):
        result=x*y
        print("---> ",result)
    def divide(self,x,y):
        result=x/y
        print("---> ",result)
    print("---------")
calculator=Calculator()
#calculator.add(10,5)
calculator.subtract(10,5)
#calculator.multiply(10,5)
#calculator.divide(10,5)