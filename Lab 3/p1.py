import random

def unique(list):
    new_list = []
    for value in list:
        if value not in new_list:
            new_list.append(value)
    return new_list

x = random.randint(0,4)
print(x)