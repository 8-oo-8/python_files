def biggest_spend_first(capacity, bookings):
    # Initialize counter objects
    accS = 0
    countC = 0
    # Sort the booking list in the reversed order by the 3rd term in each tuple,
    # so that higher spend boookings come first
    bookings.sort(key = lambda x : x[2], reverse = True)
    # Filter each booking: 1) number of people doesn't exceed capacity,
    #  2) add spend to accumulator
    for ele in bookings:
        if countC + ele[1] > capacity:
            continue
        else:
            countC += ele[1]
            accS += ele[2]
            
    return accS        

if __name__ == '__main__':
    b1 = [('Leckie', 2,20), ('Zalk', 3,20), ('Khan', 2,50), ('Aickelin', 6,80)]
    print(biggest_spend_first(5, b1))
    print(biggest_spend_first(10, b1))
    b2 = [('tom', 8,100), ('dora', 4, 100), ('huan', 4, 100)]
    print(biggest_spend_first(10, b2))
    print(biggest_spend_first(3, b2))
    b3 = [('tom', 4,100), ('dora', 4, 100), ('huan', 8, 100)]
    print(biggest_spend_first(10,b3))