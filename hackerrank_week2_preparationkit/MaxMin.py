def maxMin(k, arr):
    # Write your code here
    sortedarray = sorted(arr)  # Sort the array in ascending order
    temarr = []

    for index in range(len(arr) - k + 1):
        high = sortedarray[index + k -1]
        low = sortedarray[index]
        tem = sortedarray[index + k - 1] - sortedarray[index]
        temarr.append(tem)

    return min(temarr)


arr = [4504,1520,5857,4094,4157,3902,822,6643,2422,7288,8245,9948,2822,1784,7802,3142,9739,5629]
k = 5
maxMin(k, arr)

