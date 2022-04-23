from collections import deque
d = deque()
for i in range(int(input())):
    operation, *num = input().split(' ')
    getattr(d, operation)(*num)
for i in d:
    print(i, end=' ')
'''
getattr(object, name[, default])
object -- 對象
name -- 對象屬性
default -- 默認返回值
*num > 確保值與變量個數相同
'''
