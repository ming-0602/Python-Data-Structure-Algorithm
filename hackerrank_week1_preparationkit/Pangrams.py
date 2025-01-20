def pangrams(s):
    # Write your code here
    lowercase = s.lower()
    strip = lowercase.replace(" ", "")
    temarr = []

    for i in strip:
        if i not in temarr:
            temarr.append(i)

    if len(temarr) == 26:
        return "pangram"
    else:
        return "not pangram"

print(pangrams("The quick brown fox jumps over the lazy dog"))

