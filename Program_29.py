"""
1.Write a program which accept string from user and accept one  character. Check whether that character is present in string or not.
Input : “Marvellous Multi OS”
 e
Output : TRUE
Input : “Marvellous Multi OS”
 W
Output : FALSE

2.Write a program which accept string from user and accept one  character. Return frequency of that character.
Input : “Marvellous Multi OS”
 M
Output : 2
Input : “Marvellous Multi OS”
 W
Output : 0

3.Write a program which accept string from user and accept one  character. Return index of first occurrence of that character.
Input : “Marvellous Multi OS”
 M
Output : 0

4.Write a program which accept string from user and accept one  character. Return index of last occurrence of that character.
Input : “Marvellous Multi OS”
input: M
Output : 11

5. Write a program which accept string from user reverse that string  in place.
Input : “abcd”
Output : “dcba”
Input : “abba”
Output : “abba”
"""


class prog29:
    def prog1(self, given_str, search_char):
        chr = False
        for i in given_str:
            if i == search_char:
                chr = True
                break
        return chr

    def prog2(self,given_str, search_char):
        chr = False
        count = 0
        for i in given_str:
            if i == search_char:
                chr = True
                count+=1
                continue
        print("occurence of given character is :",count)

    def prog3(self,given_str, search_char):
        freq = 0
        for i in range(len(given_str)):
            if given_str[i] == search_char:
                freq = i
                break
        print("first occurence of given character is :", freq)

    def prog4(self,given_str, search_char):
        freq = 0
        for i in range(len(given_str)):
            if given_str[i] == search_char:
                freq = i
                continue
        print("last occurence of given character is :", freq)

    def prog5(self,given_str):
        reverse_str = ""
        for i in given_str:
            reverse_str = i + reverse_str
        print("reversed string is :", reverse_str)

obj = prog29()
input_str = input("enter a string")
chr = input("enter a character you want to search in string")
#result = obj.prog1(input_str, chr)
#if result:
#    print("found")
#else:
#    print("Not found")
obj.prog2(input_str, chr)
obj.prog3(input_str, chr)
obj.prog4(input_str, chr)
obj.prog5(input_str)