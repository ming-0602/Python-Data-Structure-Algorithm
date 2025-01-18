def find_words(input_data):
    target_word = input_data[0]
    word_list = input_data[1].replace(" ", "").split(",")

    for word1 in word_list:
        for word2 in word_list:
            # Check if the concatenation matches the target word
            if word1 + word2 == target_word:
                return f"{word1}, {word2}"

    return "No valid combination found"


# Example usage
input_data = ["baseball", "a, b, ball, base, all"]
output = find_words(input_data)
print(output)
input_data = ["abcdgef" , "a,b, abc, dgef, gef"]
print(find_words(input_data))
# print(output)  # Output: "base, ball"
