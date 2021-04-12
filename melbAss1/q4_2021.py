def potential_contacts(person_a, person_b):
    contact_loc = set()
    for entryA in person_a:
        for entryB in person_b:
            # whether in the same loc and on the same day
            if entryA[1] == entryB[1] and entryA[2] == entryB[2]:
                # earlier
                if ((entryA[5] > entryB[3] and entryA[3] < entryB[5]) or
                        ((entryA[5] == entryB[3] and entryA[6] > entryB[4]) or
                         (entryA[3] == entryB[5] and entryA[4] < entryB[6]))):

                    start_hr = max(entryA[3], entryB[3])
                    if entryA[3] == entryB[3]:
                        start_min = max(entryA[4], entryB[4])
                    elif entryA[3] < entryB[3]:
                        start_min = entryB[4]
                    else:
                        start_min = entryA[4]
                    end_hr = min(entryA[5], entryB[5])
                    if entryA[5] == entryB[5]:
                        end_min = min(entryA[6], entryB[6])
                    elif entryA[5] < entryB[5]:
                        end_min = entryA[6]
                    else:
                        end_min = entryB[6]
                    contact_loc.add((entryA[1], entryA[2], start_hr, start_min, end_hr, end_min))

    if len(contact_loc) == 0:
        return contact_loc, (0, 0)
    else:
        hours = 0
        minutes = 0
        for meet in contact_loc:
            if meet[2] == meet[4]:
                minutes += meet[5] - meet[3]
            elif meet[5] >= meet[3]:
                hours += meet[4] - meet[2]
                minutes += meet[5] - meet[3]
            else:
                hours += meet[4] - meet[2] - 1
                minutes += 60 - (meet[3] - meet[5])
        return contact_loc, (hours, minutes)

if __name__ == '__main__':
    print(potential_contacts([('Russel', 'Foodigm', 2, 9, 0, 10, 0), ('Russel', 'Afforage', 2, 10, 0, 11, 30),
                              ('Russel', 'Nutrity', 2, 11, 45, 12, 0), ('Russel', 'Liberry', 3, 13, 0, 14, 15)],
                             [('Natalya', 'Afforage', 2, 8, 15, 10, 0), ('Natalya', 'Nutrity', 4, 10, 10, 11, 45)]))
    print(potential_contacts([('Russel', 'Foodigm', 2, 9, 0, 10, 0), ('Russel', 'Afforage', 2, 10, 0, 11, 30),
                              ('Russel', 'Nutrity', 2, 11, 45, 12, 0), ('Russel', 'Liberry', 3, 13, 0, 14, 15)],
                             [('Chihiro', 'Foodigm', 2, 9, 15, 9, 30), ('Chihiro', 'Nutrity', 4, 9, 45, 11, 30),
                              ('Chihiro', 'Liberry', 3, 12, 15, 13, 25)]))
    print(potential_contacts([('Natalya', 'Afforage', 2, 8, 15, 10, 0), ('Natalya', 'Nutrity', 4, 10, 10, 11, 45)],
                             [('Chihiro', 'Foodigm', 2, 9, 15, 9, 30), ('Chihiro', 'Nutrity', 4, 9, 45, 11, 30),
                              ('Chihiro', 'Liberry', 3, 12, 15, 13, 25)]))
    print(potential_contacts([('Russel', 'Foodigm', 2, 9, 0, 10, 0), ('Russel', 'Afforage', 2, 10, 0, 11, 30),
                              ('Russel', 'Nutrity', 2, 11, 45, 12, 0), ('Russel', 'Liberry', 3, 13, 0, 14, 15)], []))
