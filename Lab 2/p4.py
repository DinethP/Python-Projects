

""" def divisible_sublist(list1, d1, d2):
    list2 = []
    for i in list1:
        if i % d1 == 0 or i % d2 == 0:
            list2.append(i)
    return list2 """

def divisible_sublist(list1, d1, d2):
        return([i for i in list1 if (i % d1 == 0 or i % d2 == 0)])

