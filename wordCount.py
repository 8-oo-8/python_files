def prevword_ave_len(word):
    text = "Call me Ishmael. Some years ago - never mind how long precisely - having little or no money in my purse, " \
           "and nothing particular to interest me on shore, I thought I would sail about a little and see the watery " \
           "part of the world. It is a way I have of driving off the spleen and regulating the circulation. Whenever " \
           "I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever " \
           "I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I " \
           "meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral " \
           "principle to prevent me from deliberately stepping into the street, and methodically knocking people's " \
           "hats off - then, I account it high time to get to sea as soon as I can. This is my substitute for pistol " \
           "and ball. With a philosophical flourish Cato throws himself upon his sword; I quietly take to the ship. " \
           "There is nothing surprising in this. If they but knew it, almost all men in their degree, some time or " \
           "other, cherish very nearly the same feelings towards the ocean with me. "
    text_list = text.split()
    pattern = """ .,-;"""
    for index in range(0, len(text_list) - 1):
        if len(text_list[index]) == 1 and text_list[index] in pattern:
            text_list[index] = ''
    for ele in text_list:
        if ele == '':
            text_list.remove(ele)
    if word not in text_list:
        return False
    wordCountTem = 0
    wordCount = 0
    lengthCountTem = 0
    lengthCount = 0
    for ele in text_list:
        if ele == word:
            wordCount += wordCountTem
            lengthCount += lengthCountTem
            wordCountTem = 0
            lengthCountTem = 0
        else:
            wordCountTem += 1
            if ele[len(ele) - 1] in pattern:
                lengthCountTem += len(ele) - 1
            else:
                lengthCountTem += len(ele)
    print(lengthCount)
    print(wordCount)
    return lengthCount / wordCount

if __name__ == '__main__':
    print(prevword_ave_len("the"))
    print(prevword_ave_len("whale"))
    print(prevword_ave_len("ship."))