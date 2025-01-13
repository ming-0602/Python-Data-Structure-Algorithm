def lonelyinteger(a):
    for i in a:
        if a.count(i) == 1:
            return i

def lonelyintegerXOR(a): #XOR method
    result = 0
    for num in a:
        result ^= num  # XOR all numbers
    return result


def lonelyintegerDictionary(a): #is like hashmap
    freq = {}
    for num in a:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    for key, value in freq.items():
        if value == 1:  # Find the lonely integer
            return key

