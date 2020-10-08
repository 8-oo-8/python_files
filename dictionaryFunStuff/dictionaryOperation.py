if __name__ == '__main__':
    list_num = [1,2,3,1,2,1,1,1,3,4,5,6]
    dic = {}
    for ele in list_num:
        if str(ele) in dic.keys():
            dic[str(ele)] += 1
        else:
            dic[str(ele)] = 1
    print(dic)        