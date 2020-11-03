"""
1. Design application for hotel. According to the management
team of hotel they are giving discount on total bill amount of
customer.
If bill bill amount is less than 500 then there is no discount , if
bill amount is less than 1500 and more than 500 they give 10%
discount.
And if the bill amount is more than 1500 then they give 15%
discount.
Our application should accept total bill amount and depends on
the discount policy we have to return the amount after applying
discount.

Input : 1200 Output : 1080
Input : 290 Output : 290
Input : 3700 Output : 3145

def CheckDiscount(bill):
    if bill<=500:
        print("sorry you are not eligible for discount")
    elif bill <= 1500 and bill >= 500:
        discountprice = bill - ((bill/100)*10)
        print("you get 10% discount and your discounted price is : ",discountprice)
    elif bill>=1500:
        discountprice = bill - ((bill / 100) * 15)
        print("you get 15% discount and your discounted price is : ", discountprice)

bill = int(input("enter the billable amount"))
CheckDiscount(bill)

2. Design application for income tax department to calculate tax
amount. According to the income tax department there is no
income tax for the income less than 5 lakhs.
If income is in between 5 to 10 lakhs then there will be 10% tax.
If income is in between 10 to 20 lakhs then there will be 20%
tax.
And for more than 20 lakhs there will be 30% tax.
We have to accept gross income from user and return the tax
amount.
Input : 600000 Output : 10000 (0 + 10000)
Input : 450000 Output : 0
Input : 1200000 Output : 90000 (0 + 50000 + 40000)

def CheckIncomeTax(GrossAmount):
    if GrossAmount<=500000:
        print("You don't have to pay income tax")
    elif GrossAmount <= 1000000 and GrossAmount >= 500000:
        IncomeTaxprice = ((GrossAmount/100)*10)
        print("you have to pay 10% Income tax and your cutting amount will be : ",IncomeTaxprice)
    elif GrossAmount>=200000:
        IncomeTaxprice = ((GrossAmount / 100) * 30)
        print("you have to pay 30% Income tax and your cutting amount will be : ",IncomeTaxprice)

GrossAmount = int(input("enter the gross amount"))
CheckIncomeTax(GrossAmount)

3. Design application for school management system.
As school is primary there are 4 standards from 1 to 4.
School fees of each standard is different.
For first standard fees are 8900, for second standard 12790, for
third standard 21000 and for fourth standard fees are 23450.
We have to accept standard from user and display the
corresponding fees.
Input : 2 Output : 12790
Input : 4 Output : 23450
Input : 6 Output : Wrong input

def CheckSchoolFees(standard):
    if standard == 1 :
        print("For 1st Standard school fee is : 8900")
    elif standard == 2:
        print("For 2nd Standard school fee is : 12790")
    elif standard == 3:
        print("For 3rd Standard school fee is :  21000")
    elif standard == 4:
        print("For 4th Standard school fee is :  23450")
    else:
        print("Wrong Input")

standard = int(input("enter the student standarda"))
CheckSchoolFees(standard)

4. We have to design application for tourist company.
Tourist company provides cars on rent.
Depends on the running of car they apply rent.
If running is less than 100 kilometres then they charge 25
rupees per kilometre .
And if running is more than 100 kilometres then they apply 15
rupees per kilometre after 100 kilometres.
We have to accept number of kilometres from user and return
the estimated rent.
Input : 73 Output : 1825
Input : 132 Output : 2980
Input : 189 Output : 3835
"""
def CheckRent(distance):
    if distance<=100:
        print("you have to pay 25rs per km so your payable amt is : ",25*distance)
    elif distance>=100:
        print("you have to pay 25rs per km so your payable amt is : ", (15 * (distance-100))+ (25 *(distance -(distance-100))))

distance = int(input("enter the no of KM"))
CheckRent(distance)
