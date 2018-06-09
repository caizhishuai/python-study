# encoding:utf-8

def arraystudy(title='世界',desc = None,*params):
    """
    数组声明
    :return 无返回值
    """
    print("print title %s" % title)
    print("params:",params)

    for n in params:
        print(n)

    if desc is None:
        print("print desc None")
    elif True:
        print("print desc %s" % desc)
    else:
        print("xxxxxxxxxxxxxx")

    arraydm1 = [1,2,'abc','ddd']
    print("output arraydm1:%s" % arraydm1)

    arraydm2 = [[1,'a'],['b','c'],['aaaa',3]]
    print("output arraydm2:%s" % arraydm2)
    return title,desc



#arraystudy('HelloWorld','MeiGuo')
#arraystudy(desc='ELuoSi')

t,d = arraystudy(33,44,55,88,12,23,42,45,62,45)

_,f = arraystudy(33,44,55,88,12,23,42,45,62,45)
print(f)






