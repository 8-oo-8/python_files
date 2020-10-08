"""
collision(program1, start1, program2, start2)
"""
def collision(program1, start1, program2, start2):
    car1 = start1
    car2 = start2
    # Initialise collisionRtn, starts with None
    collisionRtn = None 
    for i in range(0, max(len(program1), len(program2))):
        # Check whether car1 and car2 collide, if so, break the check and 
        # give the value to collisionRtn
        if (car1[0] == car2[0] and car1[1] == car2[1]):
            collisionRtn = (car1[0], car1[1])
            break

        # If there are still actions in program1, apply it to car1
        if i < len(program1):
            if program1[i] == 'Drive':
                car1 = drive(car1)
            elif program1[i] == "TurnR":
                car1 = turnR(car1)
            elif program1[i] == "TurnL":
                car1 = turnL(car1)

        # If there are still actions in program2, apply it to car2
        if i < len(program2):
            if program2[i] == 'Drive':
                car2 = drive(car2)
            elif program2[i] == "TurnR":
                car2 = turnR(car2)
            elif program1[i] == "TurnL":
                car2 = turnL(car2)   

    return collisionRtn                          


def turnR(current):
    x = current[0]
    y = current[1]
    direction = current[2]
    if direction == 'N':
        return (x, y, 'E')
    elif direction == 'E':
        return (x, y, 'S')    
    elif direction == 'S':
        return (x,y ,'W')
    else:
        return (x, y, 'N')          

def turnL(current):
    x = current[0]
    y = current[1]
    direction = current[2]

    if direction == 'N':
        return (x, y, 'W')
    elif direction == 'W':
        return (x, y, 'S')    
    elif direction == 'S':
        return (x, y, 'E')
    else:
        return (x, y, 'N') 

def drive(current):
    x = current[0]
    y = current[1]
    direction = current[2]
    
    if direction == 'N':
        return (x, y + 1, direction)
    elif direction == 'E':
        return (x + 1, y, direction)
    elif direction == 'S':
        return (x, y - 1, direction)
    else:
        return (x - 1, y, direction)  