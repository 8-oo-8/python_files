visits = [('Russel', 'Foodigm', 2, 9, 0, 10, 0),
          ('Russel', 'Afforage', 2, 10, 0, 11, 30),
          ('Russel', 'Nutrity', 2, 11, 45, 12, 0),
          ('Russel', 'Liberry', 3, 13, 0, 14, 15),
          ('Natalya', 'Afforage', 2, 8, 15, 10, 0),
          ('Natalya', 'Nutrity', 4, 10, 10, 11, 45),
          ('Chihiro', 'Foodigm', 2, 9, 15, 9, 30),
          ('Chihiro', 'Nutrity', 4, 9, 45, 11, 30),
          ('Chihiro', 'Liberry', 3, 12, 15, 13, 25)]

rtn = []
replica = set()

for i in range(len(visits)):
    name = visits[i][0]
    if not name in replica:
        same_name_list = [visits[i]]
        replica.add(visits[i][0])
        for j in range(i + 1, len(visits)):
            if name == visits[j][0]:
                same_name_list.append(visits[j])
                replica.add(visits[i][0])
        rtn.append(same_name_list)

print(rtn)
