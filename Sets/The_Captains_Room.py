K = int(input())
room_all = list(map(int, input().split()))
room_number = set()
room_more = set()
for i in room_all:
    if i in room_number:
        room_more.add(i)
    else:
        room_number.add(i)
print(sum(room_number.difference(room_more)))
