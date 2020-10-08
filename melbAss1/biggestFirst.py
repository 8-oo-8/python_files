def biggest_first(capacity, bookings):
    # TODO implement this function.
    # TO turn the list into DICTIONARY and sort from smallest.
    my_dic = {}
    for item in bookings:
        my_dic[item[0]] = item[1]
    sortlist=sorted(my_dic.values())
    
    # Add the diners from greatest to smallest.
    sortlist.sort(reverse = True)
    number = 0
    for i in sortlist:
        if number + i > capacity:
            continue
        else:
            number += i
    return number

if __name__ == '__main__':
    b1 = [('Leckie', 2), ('Zalk', 3), ('Khan', 2), ('Aickelin', 6)]
    print(biggest_first(5, b1))
    print(biggest_first(7, b1))
    b2 = [('tom', 8), ('dora', 8), ('huan', 8)]
    print(biggest_first(7, b2))
    print(biggest_first(20, b2))
