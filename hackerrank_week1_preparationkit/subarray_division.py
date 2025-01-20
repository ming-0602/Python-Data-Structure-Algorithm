def birthday(s, d, m):
    # Write your code here
    totalway = 0
    for i in range(len(s) - m + 1):
        currentsum = 0
        for j in range(m):
            currentsum += s[j + i]
        if currentsum == d:
            totalway += 1

    return totalway

#[2,3,4,5,6,7]
# let say it want 3 so it will be 2,3,4 and,3,4,5,and 4,5,6 and 5,6,7
# so is a 4 iteration so it will be len(s) -m +1
# this is like to break down which ensure only take m everytime when loop with +1 to ensure getting the last diggit
