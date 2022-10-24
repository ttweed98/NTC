import sys

facts = {"vendor":"cisco", "model":"nexus"}

print(f' The list of cmd line parameters is: {sys.argv}')

for eachfact in sys.argv[1:]:
    if eachfact in facts.keys():
        print(f' fact {eachfact} has a value of : {facts.get(eachfact)}')

    else:
        print(f' {eachfact} is not a valid key')