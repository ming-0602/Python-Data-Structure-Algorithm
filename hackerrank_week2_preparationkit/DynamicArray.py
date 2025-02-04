# Bad written question
def dynamicArray(n, queries):
    arr = []  # Start with an empty list
    for _ in range(n):  # Loop 'n' times
        arr.append([]) #create array of n size
    print(arr)

    lastAnswer = 0
    answers = []
    for q in queries:
        type_p, x, y = q
        # print(type_p, x, y)
        idx = (x ^ lastAnswer) % n
        if type_p == 1:
            arr[idx].append(y)
        elif type_p == 2:
            lastAnswer = arr[idx][y % len(arr[idx])]
            answers.append(lastAnswer)

    return answers


n = 2
queries = [
    [1, 0, 5],
    [1, 1, 7],
    [1, 0, 3],
    [2, 1, 0],
    [2, 1, 1]
]
dynamicArray(n, queries)
print(dynamicArray(n, queries))


# for(int i = 0; i < queries.Count; i++){
#             var x = queries[i][1];
#             var y = queries[i][2];
#             int queryType = queries[i][0];
#
#             int idx = ((x ^ lastAnswer) % n);
#             if(queryType == 1)
#             {
#                 Console.WriteLine(idx)                 ;
#                res[idx].Add(y);
#             }
#             else if(queryType == 2){
#                 lastAnswer = res[idx][y % res[idx].Count];
#                 answersArray.Add(lastAnswer);
#             }
#         }
#
#     return answersArray;
# }