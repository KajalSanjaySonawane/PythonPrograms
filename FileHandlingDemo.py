"""t = open("demo2.py",'r')
#print(t.read())  # all data is print and read
#print(t.readline())   #prints and read one line only

t1= open('file1','w')
print(t1.write("kajal"))  #write data to new file

t2= open('file1','a')  #append in file
for i in t:
    print(t2.write(i))
"""
t3 = open('DSC_1003.JPG','rb')
t4 = open('kajalpick.JPG','wb')    # copy image having binary data to new file
for i in t3:
    print(t4.write(i))

