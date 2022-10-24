#!/usr/bin/env python3
class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def myfunc(self):
        print ("Hi my name is " +self.name)

    def myage(self):
        print (f'I am {self.age} years old')



#----------------Instantiate the class-------------------------------------------------
user1=Person("Antonio", 28)
print(type(user1))

#------------------------Use the myfunc method of the Person class--------------------
user1.myfunc()

#------------------------Use the myage method of the Person class---------------------
user1.myage()
