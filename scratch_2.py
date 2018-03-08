def sort(number):
    number.sort()
    return number


def insert(equal,number):
    newlist = []
    for i in equal:
        if i == '<':
            newlist.append(number.pop(0))
            newlist.append('<')
        else:
            newlist.append(number.pop(-1))
            newlist.append('>')
    newlist.append(number.pop(0))
    return newlist

equal = ['<','>','<','<']
number = [1,20,9,19,16]
number = sort(number)

print(insert(equal,number))