def isSorted(word):
    for index in range(0, len(word) - 1):
        if word[index] > word[index + 1]:
            return False
    return True


def sorted_words(word_list):
    result = []
    for i in range(0, len(word_list)):
        check = True
        for j in range(0, len(word_list[i]) - 1):
            if not check:
                break
            if word_list[i][j] > word_list[i][j+1]:
                check = False
        if check:
            result.append(word_list[i])
    result.sort()
    return result

def sorted_helper(word_list):
    result = []
    for word in word_list:
        if isSorted(word):
            result.append(word)
    result.sort()
    return result


print(sorted_words((["bet", "abacus", "act", "celebration", "door"])))
print(sorted_words(['apples', 'bananas', 'spam']))
print(sorted_words(["aims", "Zip"]))
print(sorted_helper((["bet", "abacus", "act", "celebration", "door"])))
print(sorted_helper(['apples', 'bananas', 'spam']))
print(sorted_helper(["aims", "Zip"]))