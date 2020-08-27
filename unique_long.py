def unique_long_word(wlist, wlen):
    count = 0
    for word in list(set(wlist)):
        if len(word) >= wlen:
            count += 1
    return count


if __name__ == '__main__':
    print(unique_long_word(["yes","no","ng"],1))
    print(unique_long_word(["yes","yes","ng"],1))