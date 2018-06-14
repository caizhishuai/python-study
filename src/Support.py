# Filename: Support.py

def print_func( par ):
    print ("Hello : ", par)
    return

def fib(n):    # 定义到 n 的斐波那契数列
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib2(n): # 返回到 n 的斐波那契数列
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

def HaveFun():
    if __name__ == '__main__':
        print('运行的模块是 %s' % __name__)
    else:
        print('运行的模块是 %s' % __name__)