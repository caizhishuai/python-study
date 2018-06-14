s = 'Hello, Runoob'
str(s)
repr(s)
print(str(1 / 7))
x = 10 * 3.25
y = 200 * 200
s = 'x 的值为： ' + repr(x) + ',  y 的值为：' + repr(y) + '...'
print("My name is %s,%s" % ('terry','aaaaaaaaaaaa'))
print(s)

repr("My name is %s,%s" % ('terry','aaaaaaaaaaaa'))

hello = 'hello, runoob\n'
hellos = repr(hello)
print(hellos)

print(repr((x, y, ('Google', 'Runoob'))))

print('{0}网址： "{1}!"'.format('菜鸟教程', 'www.runoob.com'))

print('{0} 和 {1}'.format('Google', 'Runoob'))

