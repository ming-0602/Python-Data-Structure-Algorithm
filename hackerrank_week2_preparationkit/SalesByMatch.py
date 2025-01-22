def sockMerchant(n, ar):
    # Write your code here
    ar.sort()
    total = 0
    i = 0

    while (i < n - 1):
        if (ar[i] == ar[i + 1]):
            total += 1
            i += 2
        else:
            i += 1

    return total

print(sockMerchant(20, [4,5,5,5,6,6,4,1,4,4,3,6,6,3,6,1,4,5,5,5]))