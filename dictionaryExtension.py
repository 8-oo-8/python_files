def countWord(input_list):
    dic = {}
    for ele in input_list:
        if ele in dic.keys():
            dic[ele] += 1
        else:
            dic[ele] = 1
    return dic

if __name__ == '__main__':
    list1 = ['how','how','wuou','asdgewdas']  
    out_dictionary = countWord(list1)
    print(out_dictionary)          