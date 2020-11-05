from threading import *
from time import sleep

class first(Thread):
    def run(self):
        for i in range(10):
            print("Thread 1")
            sleep(1)

class second(Thread):  #if we have to create thread then use keyword as Thread that will import from package name 'threading'
    def run(self): #run in built fun if we change name it'll not work
        for i in range(10):
            print("Thread 2")
            sleep(1)          #for see the change use sleep bcz our processor is too fast so we can't see the changes

obj1 = first()
obj2 = second()
obj1.start()     #start is in-built fun to start the thraed
sleep(0.5)   #if both thread wake up at same time then collision is created and for avoid collision we use sleep here in two threads
obj2.start()

obj1.join()
obj2.join()    #join fun is imp to check the execution is done for sub thread and then only main thraed will complete his execution
print("exit from main thread as well after all sub threads execution is complete")