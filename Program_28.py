"""
1.Write a program which accept string from user and convert it into  lower case.
Input : “Marvellous Multi OS”
Output : marvellous multi os

2.Write a program which accept string from user and convert it into  upper case.
Input : “Marvellous Multi OS”
Output : MARVELLOUS MULTI OS

3.Write a program which accept string from user and toggle the case.
Input : “Marvellous Multi OS”
Output : mARVELLOUS mULTI os

4. Write a program which accept string from user and display only  digits from that string.
Input : “marve89llous121”
Output : 89121

"""
class prog28:
    def prog1(self,inp):
        print(inp.lower())

    def prog2(self,inp):
        print(inp.upper())

    def prog3(self,inp):
        print(inp.swapcase())

    def prog4(self,inp):
        res = []
        for i in inp:
            if 48 <= ord(i) <= 57:
                res.append(i)
        print(res)

    def prog5(self,inp):
        count = 0
        for i in inp:
            if ord(i) == 32:
                count +=1
        print("No of whitespaces in given string is :",count)

obj = prog28()
input_string = input("enter a string")
obj.prog1(input_string)
obj.prog2(input_string)
obj.prog3(input_string)
obj.prog4(input_string)
obj.prog5(input_string)