write_file1=open('subdir/newwritefile.txt', 'w')
write_file1.write("vlan" + " 100" + "\n") 
write_file1.close()


with open('newwritefile2.txt', 'w') as filevar:
    filevar.write("vlan" + " 10" + "\n")