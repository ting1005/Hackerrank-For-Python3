thousand = '(M{0,3})'
hundred = '(D?C{0,3}|CM|CD)'
ten = '(L?X{0,3}|XL|XC)'
one = '(V?I{0,3}|IV|IX)'
regex_pattern = r'^'+thousand+hundred+ten+one+'$'	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))

'''
1-3999
thousand > M(1000) MM(2000) MMM(3000)
hundred > C(100) CC(200) CCC(300) CD(400) D(500) DC(600) DCC(700) DCCC(800) CM(900)
ten > X(10) XX(20) XXX(30) XL(40) L(50) LX(60) LXX(70) LXXX(80) XC(90)
one > I(1) II(2) III(3) IV(4) V(5) VI(6) VII(7) VIII(8) IX(9)
'''
