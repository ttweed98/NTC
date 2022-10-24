# Loop through lists
# routers = ['r1', 'r2', 'r3']

# for item in routers:
#     print(item)

# Loop through dictionaries
facts = {'vendor': 'cisco', 'ip': '10.1.1.1', 'platform': 'nxos'} 

#The for loop below prints only the  values
# for fact in facts:
#     print(facts[fact])

# for each_value in facts.values():
#     print(each_value)

# for each_key in facts:
#     print(f'{each_key}:', facts[each_key])

for each_pair in facts.items():
    print(each_pair)



