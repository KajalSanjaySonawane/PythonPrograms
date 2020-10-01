"""
1)
a=10 #Global

def display():
    a=20   # Local
    print(a) #20

display()
print(a)    #10

2)
a=10
def display():
    global a    #we can change global value in local scope
    a=20   # changed global value
    print(a)   #20

display()
print(a)    #20
"""
#3. If we want global and local in one function
a=10
def display():
    a=5
    x=globals()['a']    #gives the global address of that variable here 'a'
    print(id(x))
    print("In fun value",a)  #5 Local value

    globals()['a']=50    # we can change global value in fun like this

display()
print("Outside fun value ",a)    #10,50
print(id(a))