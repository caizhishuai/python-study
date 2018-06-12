list = [1, 2, 3, 4, 5]
list.append(4)
list2 = [22, 33]
list.extend(list2)
list.sort(key=None, reverse=True)
print(list)
print(list.count(4))

# 列表当做队列使用
from collections import deque

queue = deque(list)
queue.popleft()
queue.pop()
print(queue)
queue[2] = 3
queue.append(100)

print(queue)

# 列表推导式
num = [x * 10 for x in list]
print(num)

nums = [[x, x ** 2] for x in list]
print(nums)

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
strs = [weapon.strip() for weapon in freshfruit]
print(strs)

[3 * x for x in list if x > 3]

vec1 = [2, 4, 6]
vec2 = [5, 8, -4]
vec3 = [5, 8, -4]
# print([z * y * x for x in vec1 for y in vec2 for z in vec3])
print([vec1[i] * vec2[i] for i in range(len(vec1))])

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# print([[row[i] for row in matrix] for i in range(4)])

transposed = []
for i in range(4):
    transposed.append(row[i] for row in matrix)

print(transposed)

# del

a = [-1, 1, 66.25, 333, 333, 1234.5]

del a[1]
print(a)
del a[2:4]
print(a)
del a[:]
print(a)
del a

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)

dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))

num = {x: x ** 2 for x in (2, 4, 6)}

print(num)

knights = {'gallahad': 'the pure', 'robin': 'the brave'}


def kv():
    listall = []
    for k, v in knights.items():
        listall.append(k+"-"+v)
    return listall


keyvalue = kv()
print(keyvalue)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)


questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))


for i in reversed(range(1, 10, 2)):
    print(i)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

# enumerate
# zip
# reversed
# sorted
