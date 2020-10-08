def check_move(position):
    if len(position) < 2:
        return 'The position is not valid.'
    if position[0].upper() in 'ABCDEFGH' and 1 <= int(position[-1]) <= 8:
        return 'The piece is moved to ' + position[0].upper() + str(position[1]) +'.'
    elif position[0].upper() not in 'ABCDEFGH':
        return 'The column value is not in the range a-h or A-H!'
    elif not 1<= int(position[1]) <= 8:
        return 'The row value is not in the range 1 to 8!'
    else:
        return 'The position is not valid.'

if __name__ == '__main__':
    print(check_move("B4"))