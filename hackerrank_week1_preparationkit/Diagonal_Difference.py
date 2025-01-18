def diagonal_difference(arr):
    firsttem = 0
    secondtem = 0

    for i in range(len(arr)):
        firsttem += arr[i][i]

    temlen = len(arr)-1
    for i in range(len(arr)):
        secondtem += arr[i][temlen]
        temlen -= 1

    return abs(secondtem - firsttem)


arr = [[6, 8], [-6, 9]]
#[0][0] [0][1]
#[1][0] [1][1]

#2
#15



print(diagonal_difference(arr))