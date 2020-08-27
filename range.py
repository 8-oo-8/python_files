if __name__ == '__main__':
    count = 0
    result = []
    x = range(0, 100)
    for num in x:
        if len(str(3 ** num)) == 10:
            count += 1
            result.append(num)
    for each in result:
        print(str(each) + " makes a 10-digit number")
    print("There are " + str(count) + " numbers in total")
