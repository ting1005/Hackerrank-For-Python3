import re
patten = r'^[4-6]([\d]{15}|[\d]{3}(-[\d]{4}){3})$'
patten_repeated = r'([\d])\1\1\1'
for _ in range(int(input())):
    S = input()
    TorF = re.match(patten, S)
    TorF_repeated = re.search(patten_repeated, re.sub('-', '', S))
    if TorF and not TorF_repeated: print('Valid')
    else: print('Invalid')
