# config = open('configs/switch.cfg')
# print(config.read())
# config.close()


with open('configs/switch.cfg') as configasfilevar:
    content = configasfilevar.read()
print(content)
