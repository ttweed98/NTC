listallvariables = dir()
for eachvar in listallvariables:
    if not eachvar.startswith('__'):
       value = eval(eachvar)
       print(eachvar , ':', value)