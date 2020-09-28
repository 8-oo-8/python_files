def issorted(numlist):
    if len(numlist) <= 1:
        return True
    i = 0
    for i in range(len(numlist) - 1):
        if numlist[i] > numlist[i+1]:
            return False
    return True

print(issorted([1, 45, 79, 98]))
print(issorted([-1, 8, -3, 8])) 