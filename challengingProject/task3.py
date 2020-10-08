def tolling(program, start, tolls):
    car = start
    tollCount = 0

    for action in program:
        if action == "Drive":
            car = drive(car)
            # If the car moves (change position), then check whether
            # moved into some toll position
            for toll in list(tolls.keys()):
                if car[0] == toll[0] and car[1] == toll[1]:
                    # If in the toll position, add corresponding value
                    tollCount += tolls[toll]
        elif action == "TurnL":
            car = turnL(car)
        elif action == "TurnR":
            car = turnR(car)

    return tollCount

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