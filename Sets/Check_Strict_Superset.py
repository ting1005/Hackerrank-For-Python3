SetA = set(list(map(int, input().split())))
TorF = True
for _ in range(int(input())):
    SetB = set(list(map(int, input().split())))
    if (SetA.intersection(SetB) == SetB): continue
    else: TorF = False
print(TorF)
