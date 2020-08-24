if __name__ == '__main__':
    list_a = [1,2,3,4,5,6,7,8,9,10]
    list_b = []
    for x in list_a:
        x += 1
        list_b.append(x)
    print(list_b)