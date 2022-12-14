# 8. Write a Python function that takes a list of words and returns the length of the longest one.
def longest(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]
result = longest(["Python","Programming", "Language",])
print("\nLongest word: ", result[1])
print("Length of the longest word: ", result[0])
