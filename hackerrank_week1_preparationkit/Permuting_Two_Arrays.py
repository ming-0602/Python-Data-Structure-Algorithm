#explaination
# a = [2,1,3] b=[7,8,9]
#basical try to make all equal k if true then return YES
#so to do this sort a as assending and b as reverse
#big meet small and plus together to see do it match


def twoArrays(k, A, B):
    # Write your code here
    A.sort()
    B.sort(reverse=True)

    for i in range(len(A)):
        if A[i] + B[i] < k:
            return "NO"
    return "YES"



k = 10
arr = [2, 1, 3]
arr2 = [7, 8, 9]

print(twoArrays(k, arr, arr2))