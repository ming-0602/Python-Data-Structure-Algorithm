def gridChallenge(grid):
    # Write your code here
    # sort the array element
    # compare the the a[0] < a[1]
    temlist = []
    for i in grid:
        temlist.append(len(list(i)))

    result = all(i == temlist[0] for i in temlist)
    if result is True:
        return "YES"
    else:
        return "NO"