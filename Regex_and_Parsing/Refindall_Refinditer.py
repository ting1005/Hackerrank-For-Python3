import re
string = input()
vowel = '[AEIOUaeiou]'
consonants = '[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]'
pattern = r'(?<=' + consonants + ')(' + vowel + '{2,})' + consonants
L = re.findall(pattern, string)
if L == []: print('-1')
else:
    for i in L:
        print(i)
