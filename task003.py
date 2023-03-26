# Sample Input:
# ["eat", "tea", "tan", "ate", "nat", "bat"]

# Sample output
# [["ate", "eat", "tea"], ["nat", "tan"], ["bat"]]

# т.е. сгруппировать слово по "общим буквам"


input = ("eat", "tea", "tan", "ate", "nat", "bat")
print(input)


def f_dictionary(words: list[input]) -> list[list[input]]:
    dict = {}
    for i in words:
        key = "".join(sorted(i))
        if key not in dict:
            dict[key] = []

        dict[key].append(i)

    return list(dict.values())


output = f_dictionary(input)
print(output)
