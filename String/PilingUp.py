for i in range(int(input())):
    block_size = input()
    blocks = [int(i) for i in input().split(' ')]
    min_list = blocks.index(min(blocks))
    left_blocks = blocks[:min_list]
    right_blocks = blocks[min_list+1:]
    if left_blocks == sorted(left_blocks, reverse=True) and right_blocks == sorted(right_blocks):
        print('Yes')
    else:
        print('No')
