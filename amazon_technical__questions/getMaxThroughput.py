#question
#array find from group of 3 in each group so is len 8 array can form 2 group
#find media of groups then plus together , retunr the value
#example
#[8,6,3,4,4,5,6]
#correct answer [8,6,3] [4,5,6]
# 6 + 5 = 11
#return 11

def getMaxThroughput(host_throughput):#wrong algo
    # Write your code here
    n = len(host_throughput)
    print(n)

    host_throughput.sort(reverse=True)

    system_throughput = 0
    for i in range(1, n, 3):  # skip 3
        system_throughput += host_throughput[i]

    return system_throughput

arr = [8, 6, 3, 4, 4, 5,6]

print(getMaxThroughput(arr))