lines = input("Enter the triangle height: ")
for current in range(0, int(lines)):
    output = ""
    for i in range(0,int(lines) - current):
        output += "*"
    for i in range(0, 2 * current + 1):
        output += " "
    for i in range(0, int(lines) - current):
        output += "*"
    print(output)
for current in range(1, int(lines)):
    output = ""
    for i in range(0, current + 1):
        output += "*"
    for i in range(0, 2 * int(lines) - 2 * current - 1):
        output += " "
    for i in range(0, current + 1):
        output += "*"
    print(output)    
