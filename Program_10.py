"""
Assignment : 10
1.Write a program which accept radius of circle from user and calculate its area.  Consider value of PI as 3.14. (Area = PI * Radius * Radius)
Input : 5.3
Output : 88.2026

def calcualtearea(rad):
    return 3.14*rad*rad

rad=float(input("enter a rad"))
res= calcualtearea(rad)
print("area of given radius is :", "{:.4f}".format(res))

2. Write a program which accept width & height of rectangle from user and calculate  its area. (Area = Width * Height)
Input : 5.3 9.78
Output : 51.834

def calculatearea(height,width):
    return width*height

height= float(input("enter height"))
width = float(input("enter width"))
res= calculatearea(height,width)
print("area of rectangle is",round(res,4))

3. Write a program which accept distance in kilometre and convert it into meter. (1  kilometre = 1000 Meter)
Input : 5
Output : 5000

def calculatekm(km):
    return km*1000
km=int(input("enter distance"))
res = calculatekm(km)
print("km to meter is:",res)

4. Write a program which accept temperature in Fahrenheit and convert it into  celsius. (1 celsius = (Fahrenheit -32) * (5/9))
Input : 10
Output : -12.2222 (10 - 32) * (5/9)
Input : 34
Output : 1.11111 (34 - 32) * (5/9)

def converttocelsius(temr):
    return (temr - 32) * (5/9)

temr=int(input("enter temp in fahrenheit"))
res = converttocelsius(temr)
print("temp converted from fagrenheit to celsius is:",round(res,4))

5. Write a program which accept area in square feet and convert it into square  meter. (1 square feet = 0.0929 Square meter)
Input : 5
Output : 0.464515
Input : 7
Output : 0.650321
"""
def converttosquaremeter(num):
    return num*0.0929

num=int(input("enter no in sq ft"))
res = converttosquaremeter(num)
print("square feet converted to square meter is:",round(res,4))
