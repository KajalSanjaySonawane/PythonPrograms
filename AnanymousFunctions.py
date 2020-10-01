from functools import reduce    #for reduce we require package functools

"""1)
f= lambda x:x*2         # lambda x: x*2 is a expression we can only give one expression to argument
# here f is function object
print(f(5))  #we are not calling different function name we used here lambda i.e. Anonymous function

2)"""
#we can use lambda function with map,filter,reduce,etc (Built-in functions)

my_list = [1,2,5,6,4,8,3,2,4]

new_list = list(filter(lambda x: x%2==0,my_list))  #filter gives if true condition satisfies
print(new_list)

new_list1 = list(map(lambda a: a*2,new_list))    #map will iterate through all items of list
print(new_list1)



new_list2 = list(reduce(lambda a,b: a+b, new_list1))
print(new_list2)