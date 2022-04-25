import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []
string = ''
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

for i in range(m):
    for L in matrix:
        string += L[i]

print(re.sub(r'([a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])', r'\1 ', string))
'''
r'\1 ' > the first groupp matched in the pattern (r'\1)
'''
