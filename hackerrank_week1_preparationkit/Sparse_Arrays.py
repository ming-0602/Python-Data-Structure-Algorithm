def matchingStrings(strings, queries):
    result = []
    for str in queries:
        tem = 0
        for str2 in strings:
            if (str2 == str):
                tem+=1
        result.append(tem)
        tem==0
    return result