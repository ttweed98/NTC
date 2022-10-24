import os
#import time
#import xmltodict

#print(dir(time))


#key5: {'subkey1': 'ISE', 'subkey2':'FirePower'}
#print(type('subkey1'))

dict10 = {'key1':'IOS', 'key2': 'NXOS', 'key3':'IOS-XE', 'key4': 'IOS_XR','key5': {'subkey1': 'ISE', 'subkey2':'FirePower'}}
print(dict10['key3'])





# dict1['key5']['subkey1'] = 'ASA'
#print(dict1['key5']['subkey2'])
for eachfiredevice in dict1['key5']['subkey2']:
    print(eachfiredevice)


#value1=dict1['key2']
#print(dict1['key5']['subkey1'])
for each_key in dict1:
  print(str(dict1[each_key]) + '\n') 
  print('\n') 
  print(os.linesep)
# 
# answer=dict1['key1']
#print(dict1['key1'])

#---------This prints value of specific key in dictionary-------------------------
#print(f' The value of 1st key is {answer}')

#------------------A way to print keys and value together----------------------
#for i in dict1:
  #print (i , dict1[i])

#-------------------Another way to print keys and value-----------------------------
#for k, v in dict1.items():
#  print(k, v )
#print(os.linesep)
 
  
  

#-----------------Another way to print key and value  only in python2------------------------------

#for k, v in dict1.iteritems():
#  print(k, v)

#----------------A way to print key and values in a tuple pair
#for eachpair in dict1.items():
#  print(eachpair)
#print(os.linesep)

#------------------Print only keys in the dictionary----------
#for eachkey in dict1.keys():
#  print(eachkey)
#print(os.linesep)

#------------------Print only values in the dictionary------------
#for eachvalue in dict1.values():
#  print(eachvalue)
#print(os.linesep)