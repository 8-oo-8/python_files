def change_list(l):
    tem = l[0]
    for n in range(0,len(l) - 1):
        l[n] = l[n+1]
    l[len(l) - 1] = tem
    return l
print(change_list([1,2,3,4,5,'d']))
