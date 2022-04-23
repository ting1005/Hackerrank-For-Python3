import string
def print_rangoli(size):
    # your code goes here
    alpha = string.ascii_lowercase
    
    for i in range(size-1, 0, -1):
        line_r = '-'.join(alpha[i:size])
        line_l = ''.join(reversed(line_r[1:]))
        line_add = line_l + line_r
        print(line_add.center(4*size-3, '-'))
        
    for i in range(size):
        line_r = '-'.join(alpha[i:size])
        line_l = ''.join(reversed(line_r[1:]))
        line_add = line_l + line_r
        print(line_add.center(4*size-3, '-'))
    
 
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
