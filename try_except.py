
list1=[1,2,3]
#print(list1[2])



"""try:
    print(list1[3])
    
except Exception as x:
    print("An exception error has occurred")
    print(x)"""


y = 400
try:
    if y != 300:
        print(" Y value is 300")
        raise Exception("Experiment on Raising an Exception")
        
except Exception as e:
        print("learning about forced Exceptions")
        print(e)

