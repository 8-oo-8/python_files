"""
navigate(program, start)
"""
def navigate(program, start):
    rtn = start
    for action in program:
        if action == 'Drive':
            rtn = drive(rtn)
        elif action == 'TurnR':
            rtn = turnR(rtn)
        elif action == 'TurnL':
            rtn = turnL(rtn)
    return rtn               

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