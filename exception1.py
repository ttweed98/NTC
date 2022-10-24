devices = ['r1', 'r2', 'r3']
try:
    print (devices["r4"])
except Exception as err_msg:
    print ('Insert custom code...')
    print ('Error from Python:', err_msg)


