import re
num = int(input())
and_patten = r'(?<= )(&&)(?= )'
or_patten = r'(?<= )(\|\|)(?= )'
for i in range(num):
    print(re.sub(and_patten, 'and', re.sub(or_patten, 'or', input())))
