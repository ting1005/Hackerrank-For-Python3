_, M = input(), set(list(map(int, input().split())))
_, N = input(), set(list(map(int, input().split())))
m = M.difference(N)
m.update(N.difference(M))
m = sorted(m)
for i in m : print(i)