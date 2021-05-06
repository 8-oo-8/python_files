import csv

file = open('csv_file.csv')
data = csv.reader(file)
head = next(data)
for row in data:
    print(row)
    print('2' in row)
    print('7' in row)
for row in data:
    print(row)
    print('2' in row)
    print('7' in row)