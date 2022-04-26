for _ in range(int(input())):
    _, SetA = input(), set(list(map(int, input().split())))
    _, SetB = input(), set(list(map(int, input().split())))
    print(SetA.intersection(SetB) == SetA)
