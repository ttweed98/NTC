def is_greater(a,b):
  # returns True if a is greater
  if a<b:
    return False
  return True





























def test_is_greater():
  assert is_greater(8,9)==True

def add_result(x,y):
  result=x+y
  print(" A print line before return within a function")
  return result
  print(" A print line after return within a function will not print")


#output=is_greater(11,9)
#print(output)



if __name__=="__main__":
    # output is True
    #print (is_greater(5,5))
    # TypeError
    #print(is_greater(5, "four"))
    #print(is_greater(6,7))

    #print('------------------------------------------------------')
    #print(is_greater(12,10))
    
    #print('------------------------------------------------------')
    #print(is_greater())

    answer=add_result(3,4)
    print(answer)

    


    
