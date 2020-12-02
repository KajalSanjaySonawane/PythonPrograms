"""
1. Write a program which displays ASCII table. Table contains symbol,  Decimal, Hexadecimal and
 Octal representation of every member from  0 to 255.

2. Accept character from user. If character is small display its  corresponding capital character,
 and if it small then display its  corresponding capital. In other cases display as it is.
Input : Q
Output : q
Input : m
Output : M
Input : 4
Output : 4
Input : %
Output : %

3. Accept character from user. If it is capital then display all the  characters from the
input characters till Z. If input character is small  then print all the characters in reverse
order till a. In other cases  return directly.
Input : Q
Output : Q R S T U V W X Y Z
Input : m
Output : m l k j i h g f e d c b a  Input : 8
Output :

4. Accept Character from user and check whether it is special symbol  or not (!, @, #, $, %, ^, &, *).
Input : %
Output : TRUE
Input : d
Output : FALSE

"""
class prog26:
    def prog1(self,n):
        w = len(bin(n)) - 2
        for i in range(1, n + 1):
            print('{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}'.format(i, width=w))

    def prog2(self,char):
        print(char.swapcase())

    def prog3(self,char):
        if 97 <= ord(char) <= 122:
            mid = (97 + 122)//2
            if ord(char) >= mid:
                for j in range(ord(char),123):
                    print(chr(j))

            elif ord(char) <= mid:
                for i in range(ord(char),96,-1):
                    print(chr(i))

        elif 65 <= ord(char) <= 90:
            mid = (65 + 90) // 2
            if ord(char) >= mid:
                for j in range(ord(char), 91):
                    print(chr(j))

            elif ord(char) <= mid:
                for i in range(ord(char), 64, -1):
                    print(chr(i))

    def prog4(self,char):
        if ord(char) == 64 or ord(char) == 94 or ord(char) == 33 or ord(char) == 36 or ord(char) == 37 or ord(char) == 38 or ord(char)==42:
            print("True")
        else:
             print("False")

    def prog5(self,char):
        res = ord(char)
        print(res, hex(res), bin(res), oct(res))

obj = prog26()
#n = int(input("enter the last range"))
#obj.prog1(n)
char = input("enter a character")
#obj.prog2(char)
#obj.prog3(char)
#obj.prog4(char)
obj.prog5(char)

