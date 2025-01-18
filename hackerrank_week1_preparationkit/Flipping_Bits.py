def flippingBits(n):
    # Write your code here
    tem = f"{n:032b}"
    intolist = list(tem)
    flipped_list = []
    for i in intolist:
        if(i == '0'):
            flipped_list.append('1')
        else:
            flipped_list.append('0')

    print(flipped_list)
    flipped_binary = "".join(flipped_list)

    return int(flipped_binary, 2)



print(flippingBits(42))