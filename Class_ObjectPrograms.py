"""1.basic

class computer:     #create class name as computer
    def com1(self):  #self means passing the object itself in this case obj1
        print("Hello this is my first class")

obj1 = computer()   #Creating an object obj1 of class computer
computer.com1(obj1)
obj1.com1()
"""

class calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self, a, b):
        print("addition is :", a+b)

obj1 = calculator(2,4)
obj1.add(2, 4)
