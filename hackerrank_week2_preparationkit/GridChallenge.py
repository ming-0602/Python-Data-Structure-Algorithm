def gridChallenge(grid):
    # Write your code here
    # sort the array element
    # compare the the a[0] < a[1]
    for i in grid:
        temchararr = list(i)
        # print(temchararr.sort())
        sortedtemchar = sorted(temchararr)
        print(sortedtemchar)
        index = 0
        while (index < sortedtemchar.size()):
            if (sortedtemchar[index + 1] - sortedtemchar[index] != 1):
                return "NO"
            index += 1

    return "YES"

grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']

gridChallenge(grid)