import sys
import Support
from testpackage import class_b
#from Support import fib, fib2
#from Support import *

print("命令行参数如下:")
for i in sys.argv:
    print(i)

print('Python 路径为：', sys.path)

# Support.print_func('caizhishuai')

# Support.fib(100)

# from…import 语句
# fib(100)

def HaveFun():
    if __name__ == '__main__':
        print('I am in my domain,my name is %s' % __name__)
    else:
        print('Someone else calls me!,my name is %s' % __name__)

Support.HaveFun()
HaveFun()

# dir

print(dir(sys))
# 包的概念
class_b.hello()
