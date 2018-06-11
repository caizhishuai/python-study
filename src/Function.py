def Hello():
    print('Hello')


Hello()


def area(width, height):
    return width * height


sum = area(8, 189)
print(sum)

a = 15


def ChangeInt(a):
    a = 10


b = 2
ChangeInt(b)
print(b)
print(a)


def changeme(mylist):
    mylist.append([1, 2, 3, 4])
    print(mylist)
    return

mylist = [11, 22, 33]
changeme(mylist)
print(mylist)
