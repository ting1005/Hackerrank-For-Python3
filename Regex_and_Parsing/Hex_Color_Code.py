import re
N = int(input())
patten = r':?.(#[A-Fa-f0-9]{6}|#[A-Fa-f0-9]{3})'
for _ in range(N):
    m = re.findall(patten, input())
    for i in m: print(i)
