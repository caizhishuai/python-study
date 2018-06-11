d = {'Alice': 1, 'Beth': 2}
dict2 = {'abc': 123, 98.6: 37};
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print(dict2)

print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])

# print ("dict['Alice']: ", dict['Alice'])

dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8;
dict['School'] = "菜鸟教程"  # 添加信息
print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])

del dict['Name']  # 删除键 'Name'

dict.clear()
print(dict)
del dict

dict3 = {'Name': 'Runoob', 'Age': 7}
print("dict3['Name']: ", dict3)

print(len(dict3))

print(str(dict3))

print(type(dict3))

cities = {
    '北京': {
        '朝阳': ['国贸', 'CBD', '天阶', '我爱我家', '链接地产'],
        '海淀': ['圆明园', '苏州街', '中关村', '北京大学'],
        '昌平': ['沙河', '南口', '小汤山', ],
        '怀柔': ['桃花', '梅花', '大山'],
        '密云': ['密云A', '密云B', '密云C']
    },
    '河北': {
        '石家庄': ['石家庄A', '石家庄B', '石家庄C', '石家庄D', '石家庄E'],
        '张家口': ['张家口A', '张家口B', '张家口C'],
        '承德': ['承德A', '承德B', '承德C', '承德D']
    }
}

print(cities['北京']['密云'])

for c in cities:
    print(c)

a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a + b
