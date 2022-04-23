import re
for _ in range(int(input())):
    string = input()
    TorF = bool(re.match(r'^[+-]?[0-9]*[.][0-9]+$', string))
    print(TorF)
    
'''
 re.search() > scans through a string
 re.match() > only matches
 
Explain : ^[+-]?[0-9]*[.][0-9]+$
 ^ > Start of Line
 [+-]? > start with either + or - ('?' is or)
 [0-9]* > any number from 0-9, it can repeat 0 times ('*' is repeat 0 times or more)([0-9] can equal to \d)
 [.] > must have '.'
 [0-9]+ > any number from 0-9, it can repeat 1 times(least 1 times) ('+' is repeat 1 times or more)([0-9] can equal to \d)
 $ > End of line
 '''
