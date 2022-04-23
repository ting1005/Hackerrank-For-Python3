def print_formatted(number):
    # your code goes here
    tab = number.bit_length()
    for i in range(1, number+1):
        print(f'{i:{tab}d} {i:{tab}o} {i:{tab}X} {i:{tab}b}')
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
