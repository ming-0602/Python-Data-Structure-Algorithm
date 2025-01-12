def timeConversion(s):
    # Write your code here
    splited_string = list(s)
    size = len(splited_string)

    if (splited_string[size - 2] == "P"):
        if not (splited_string[0] == "1" and splited_string[1] == "2"):
            combine = "".join(splited_string[0] + splited_string[1])
            res = int(combine) + 12
            sperated = list(str(res))
            splited_string[0] = sperated[0]
            splited_string[1] = sperated[1]

    else:
        if (splited_string[0] == "1" and splited_string[1] == "2"):
            splited_string[0] = "0"
            splited_string[1] = "0"

    splited_string.pop(size - 1)
    splited_string.pop(size - 2)
    result = "".join(splited_string)
    return result
