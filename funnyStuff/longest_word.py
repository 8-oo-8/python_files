def long_high_word(wordlist):
    '''
    dict_length = dict.fromkeys(wordlist, (0, 0))
    for key in dict_length.keys():
        dict_length[key] = (len(key), ord(key[0]))
    dict_length = dict(sorted(dict_length.items(), key=lambda x:x[1][1], reverse=True))
    dict_length = dict(sorted(dict_length.items(), key=lambda x:x[1][0], reverse=True))
    return list(dict_length.keys())[0]
    '''
    longest = 0
    for element in wordlist:
        if len(element) > longest:
            longest = len(element)
    options = []
    for element in wordlist:
        if len(element) == longest:
            options.append(element)
    if len(options) > 1:
        options.sort(reverse=True)
    return options[0]

print(long_high_word(['a', 'cat', 'sat']))
print(long_high_word(['saturation', 'of', 'colour']))
print(long_high_word(['abc', 'bc', 'c']))
print(long_high_word(['samIam']))