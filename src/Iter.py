'''
list = [1, 2, 3, 4]
# 创建迭代器对象
it = iter(list)
# 输出迭代器的下一个元素
print(next(it))
# 输出迭代器的下一个元素
print(next(it))

while True:
    try:
        print (next(it))
    finally:
        exit()


for x in it:
    print (x, end=" ")




def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        exit()

'''


def testit():
    list = [1, 23, 4, 5]
    for l in list:
        yield l


fn = testit()
# print("type ", type(fn))
# print(help(fn))
# print(fn)
print(next(fn, None))

for t in testit():
    cur = next(fn, None)
    if cur is None:
        print("End")
    else:
        print(cur)

list = [1, 2, 3, 4]
it = iter(list)
'''
while True:
    print(next(it,"111"), end=",")
'''


def ChangeInt(a):
    print(a)
    a = 10
    print(a)


b = 2
print(b)
ChangeInt(b)
print(b)


def printinfo(name, age):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return "123"


print(printinfo('', ''))


def functionname(arg1, *arg2):
    print(arg2)
    return arg1, arg2


result = functionname(1, 2, 3, 4, 5, 6)

print(result[1])


def printinfo(arg1, *vartuple):
    print("输出")
    print(arg1)
    print("第二次输出")
    for i in vartuple:
        print(i)
    return

printinfo( 10 )
printinfo( 70, 60, 50 )

# 匿名函数
sum = lambda arg1, arg2: arg1 + arg2

print(sum(2,3))

# 变量作用域
'''
L （Local） 局部作用域
E （Enclosing） 闭包函数外的函数中
G （Global） 全局作用域
B （Built-in） 内建作用域

查找规则:  L –> E –> G –>B
'''

x = int(2.9)  # 内建作用域
g_count = 0  # 全局作用域

def outer():
    o_count = 1  # 闭包函数外的函数中
    def inner():
        i_count = 2  # 局部作用域

if True:
    msg="我在if里"
print(msg)

class T:
    message = 'a'

num = 1
def fun1():
    global num  # 需要使用 global 关键字声明
    print(num)
    num = 123
    print(num)
fun1()

def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明
        num = 100
        print(num)
    inner()
    print(num)
outer()


