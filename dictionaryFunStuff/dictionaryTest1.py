def repeat_word_count(text, n):
    dic = {}
    tem = text.split()
    res = []

    for i in tem:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1  
            
    for key in dic.keys():
        if dic[key] >= n:
            res.append(key)    
    res.sort()                  
    return res

print(repeat_word_count("buffalo buffalo buffalo buffalo", 2))