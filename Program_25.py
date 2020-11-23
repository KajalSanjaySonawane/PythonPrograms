"""
1. Accept Character from user and check whether it is alphabet or not  (A-Z a-z).
Input : F
Output : TRUE
Input : &
Output : FALSE

2. Accept Character from user and check whether it is capital or not  (A-Z).
Input : F
Output : TRUE
Input : d
Output : FALSE

3. Accept Character from user and check whether it is digit or not  (0-9).
Input : 7
Output : TRUE
Input : d
Output : FALSE

4. Accept Character from user and check whether it is small case or  not (a-z).
Input : g
Output : TRUE
Input : D
Output : FALSE

5. Accept division of student from user and depends on the division  display exam timing. There are 4 divisions in school as A,B,C,D. Exam  of division A at 7 AM, B at 8.30 AM, C at 9.20 AM and D at 10.30 AM.  (Application should be case insensitive)
Input : C
Output : Your exam at 9.20 AM
Input : d
Output : Your exam at 10.30 AM
"""
class prog25:
    def prog1(self,char):
        if 97 <= ord(char) <= 122 or 65 <= ord(char) <= 90:
            return True
        else:
            return False

    def prog2(self,char):
        if char.upper() == char or 65 <= ord(char) <= 90:
            print("enter character is Capital")
        else:
            print("enter character is lower")

    def prog3(self,char):
        if 48 <= ord(char) <= 57:
            print("it is digit")
        else:
            print("It is not digit")

    def prog4(self,char):
        if char.lower() == char or 97 <= ord(char) <= 122:
            print("enter character is lower")
        else:
            print("enter character is Capital")

    def prog5(self,div):
        if ord(div) == 65 or ord(div) == 97:
            print("Your exam at 7 AM")
        elif ord(div) == 66 or ord(div) == 98:
            print("Your exam at 8:30 AM")
        elif ord(div) == 67 or ord(div) == 99:
            print("Your exam at 9 AM")
        elif ord(div) == 68 or ord(div) == 100:
            print("Your exam at 9:30 AM")

obj = prog25()
char = input("enter any character")
ans = obj.prog1(char)
if ans:
    print("enter character is alphabet")
else:
    print("enter character is not alphabet")

obj.prog2(char)
obj.prog3(char)
obj.prog4(char)
div = input("enter your division from A,B,C,D")
obj.prog5(div)
