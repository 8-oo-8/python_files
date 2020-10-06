def listCompre(x, y, z, n):
    tem = []

    for i in range(0, x + 1):
        for j in range(0, y + 1):
            for k in range(0, z + 1):
                tem.append([i, j, k])

    return [sub for sub in tem if sum(sub) != n]

print(listCompre(1,1,1,2))
print(listCompre(2,2,2,2))                    