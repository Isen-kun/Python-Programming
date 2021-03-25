string = input('Enter a string: ')
lr = 0
ur = 0
dt = 0
sp = 0
for i in string:
    if i.isupper():
        ur += 1
    elif i.islower():
        lr += 1
    elif i.isdigit():
        dt += 1
    elif i == ' ':
        sp += 1
print('The number of uppercase letters:', ur)
print('The number of lowercase letters:', lr)
print('The number of digits:', dt)
print('The number of whitespace characters:', sp)
