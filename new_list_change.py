import copy

def cycle(input_list):
    new_list = copy.copy(input_list)
    tem = new_list[0]
    for n in range(0,len(new_list) - 1):
        new_list[n] = new_list[n+1]
    new_list[len(new_list) - 1] = tem
    return new_list

print(cycle([1,2,3,4,5,'d']))
