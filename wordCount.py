def top5_word(text):
    text_list = text.split()
    dic = {}
    rtn = []
    for word in text_list:
        if word in dic.keys():
            dic[word] +=1;
        else:
            dic[word] = 1
    tem = list(dic.items())
    tem.sort(key = lambda x : x[0])
    tem.sort(key = lambda x : x[1], reverse = True) 
    if len(tem) >= 5:
        for i in range(0,5):
            rtn.append(tem[i][0])
    else:
        for i in range(0,len(tem)):
            rtn.append(tem[i][0])        
    return rtn

if __name__ == '__main__':
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
    print(top5_word(text))