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


