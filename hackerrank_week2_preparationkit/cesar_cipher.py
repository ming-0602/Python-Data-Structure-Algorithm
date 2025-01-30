def caesarCipher(s, k):
    # Write your code here
    dictionary = "abcdefghijklmnopqrstuvwxyz"
    splitlist_dictionary = list(dictionary)

    result = ""
    for i in list(s):
        if(i.isupper()):
            tem = splitlist_dictionary.index(i.lower())
            new_index = (tem + k) % len(splitlist_dictionary)
            result += splitlist_dictionary[new_index].upper()
        elif(i.islower()):
            tem = splitlist_dictionary.index(i)
            new_index = (tem + k) % len(splitlist_dictionary)
            result += splitlist_dictionary[new_index]
        else:
            result += i

    return print(result)


s="Always-Look-on-the-Bright-Side-of-Life"
k=5

caesarCipher(s, k)


s="Hello_World!"
k=4
caesarCipher(s, k)

s="www.abc.xy"
k=87
caesarCipher(s, k)