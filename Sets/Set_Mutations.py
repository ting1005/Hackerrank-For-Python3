_, A = input(), set(list(map(int, input().split())))
for _ in range(int(input())):
    command = input().split()
    B = set(list(map(int, input().split())))
    getattr(A, command[0])(B)
print(sum(A))
