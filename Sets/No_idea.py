n, m = map(int, input().split())
N = list(map(int, input().split()))
A = set(list(map(int, input().split())))
B = set(list(map(int, input().split())))
total = 0
for i in N:
    if i in A : total+=1
    if i in B : total-=1
print(total)
