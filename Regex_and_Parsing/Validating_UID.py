import re
length = r'[a-zA-Z0-9]{10}'
upper = r'(.*[A-Z]){2,}'
digits = r'(.*[0-9]){3,}'
no_repeat = r'.*(.).*\1.*'
for _ in range(int(input())):
    UID = input()
    TorF1 = bool(re.match(length, UID))
    TorF2 = bool(re.match(upper, UID))
    TorF3 = bool(re.match(digits, UID))
    TorF4 = bool(re.match(no_repeat, UID))
    
    if TorF1 and TorF2 and TorF3 and not TorF4: print('Valid')
    else :print('Invalid')
