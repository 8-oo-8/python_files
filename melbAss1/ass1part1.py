# Enable the usage of *combinations* function in below
from itertools import combinations

def exhaustive_search_exhaustive(capacity,bookings):
    tem = []
    # Extract number of guests from each booking
    for ele in bookings:
        tem.append(ele[1])
    res = []
    # Find all possible combinations of guest numbers
    for i in range(1,len(tem) + 1):
        res += list(combinations(tem, i))
    optimizaion = 0
    # Filter the largest possible number of guests under the required condition
    for ele in res:
        if sum(ele) > optimizaion and sum(ele) <= capacity:
            optimizaion = sum(ele)

    return optimizaion             
                



if __name__ == '__main__':
    b1 = [('Leckie', 2), ('Zalk', 3), ('Khan', 2), ('Aickelin', 6)]
    print(exhaustive_search_exhaustive(5, b1))
    print(exhaustive_search_exhaustive(7, b1))
    b2 = [('tom', 8), ('dora', 8), ('huan', 8)]
    print(exhaustive_search_exhaustive(7, b2))
    print(exhaustive_search_exhaustive(20, b2))