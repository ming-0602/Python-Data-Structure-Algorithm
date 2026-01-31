# def main(p):
#     result = []
#     len_of_arr = len(p)
#     result.append(1)
#     k = 1
#     location_of_one = p.index(1)
#
#     for i in range(1,len_of_arr+1):
#
#         temuse = []
#         for j in range(len_of_arr - k + 1):
#             tem = []
#             for l in range(k):
#                 tem.append(p[l + j])
#                 # print(tem)
#             temuse.append(tem)
#
#         for slice_data in range(len(temuse)):
#             if k in temuse[slice_data]:
#                 result.append(1)
#                 k+=1
#                 break
#             else:
#                 result.append(0)
#                 break
#
#
#     return print(result)
# from dsa.searchalgo.binarysearch import result


# temuse = []
    # for i in range(len_of_arr - k + 1 ):
    #     tem=[]
    #     for j in range(k):
    #         tem.append(p[i + j])
    #         # print(tem)
    #     temuse.append(tem)

        # print(tem)
    # print(temuse)



# def main(p):
#     result = []
#     n = len(p)
#
#     for k in range(1, n + 1):
#         found = 0
#         # build all subarrays of length k
#         for i in range(n - k + 1):
#             subarray = []
#             for j in range(k):
#                 subarray.append(p[i + j])
#             # check if subarray contains the number k
#             print(subarray)
#             if k in subarray:
#                 found = 1
#                 break
#         result.append(found)
#
#     return result



def main(p):
    size_of_list = len(p)
    mapping = []
    result = []

    for k in range(1, size_of_list + 1):
        mapping.append(k)
        answer = 0

        for i in range(size_of_list - k + 1):
            tem2 = []
            for j in range(k):
                tem2.append(p[j + i])

            if mapping == sorted(tem2):
                answer = 1
                break

        result.append(answer)

    return "".join(map(str, result))


# temuse = []
    # for i in range(len_of_arr - k + 1 ):
    #     tem=[]
    #     for j in range(k):
    #         tem.append(p[i + j])
    #         # print(tem)
    #     temuse.append(tem)

        # print(tem)
    # print(temuse)


p = [5,3,1,2,4]
print(main(p))