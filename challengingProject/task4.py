def whiley(program, location):
    car = location
    index = 0

    while(index < len(program)):
        # Find the start of Whiley
        if (program[index] == 'Whiley'):
            # Loop the action until the predicate is true
            while interpreter(program[index + 1], car):
                # Find the position closest to the current Whiley
                end = program.index('EndWhiley', index)
                # Do the actions in the Whiley loop
                for i in range(index + 2, end):
                    if program[i] == 'Drive':
                        car = drive(car)
                    elif program[i] == 'TurnL':
                        car = turnL(car)
                    else:
                        car = turnR(car)     
            # Continue iterate the program list            
            index = end + 1
        else:
            # Here are normal application of vehicle movement
            if program[index] == 'Drive':
                car = drive(car)
            elif program[index] == 'TurnL':
                car = turnL(car)
            else:
                car = turnR(car)  
            index += 1                      
        
    return car


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

"""
This function helps check the Whiley loop predicate
will return true if the condition is satisfied, and vice versa.
"""
def interpreter(listPredicate, current):
    varA = listPredicate[0]
    symbol = listPredicate[1]
    varB = listPredicate[2]

    if symbol == 'LT':
        if varA == 'X':
            return current[0] < varB
        else:
            return current[1] < varB
    elif symbol == 'GT':
        if varA == 'X':
            return current[0] > varB
        else:
            return current[1] > varB
    elif symbol == 'EQ':
        return current[2] == varB
    else:
        return current[2] != varB    
