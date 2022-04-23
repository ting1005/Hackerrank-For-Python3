from collections import OrderedDict
n = int(input())
item_dict = OrderedDict()

for i in range(n):
    item, price = input().rsplit(' ', 1) # A B C > [AB , C]
    item_dict[item] = item_dict.get(item, 0) + int(price)


for key, value in item_dict.items():
    print(key, value)
