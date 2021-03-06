numbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9')


def score(game):
    result = 0
    frame = 1
    in_first_half = True
    for i in range(len(game)):
        if game[i] == '/':
            result += 10 - last
        else:
            result += get_value(game[i])
        if frame < 10 and get_value(game[i]) == 10:
            result = tens_handler(game, result, i)
        last = get_value(game[i])
        if not in_first_half:
            frame += 1
        if in_first_half:
            in_first_half = False
        else:
            in_first_half = True
        if game[i] == 'X' or game[i] == 'x':
            in_first_half = True
            frame += 1
    return result


def get_value(char):
    if char in numbers:
        return int(char)
    elif char == 'X' or char == 'x' or char == '/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()


def tens_handler(game, result, i):
    result += get_value(game[i+1])
    if game[i] == 'x' or game[i] == 'X':
        if game[i+2] == '/':
            result += 10 - get_value(game[i+1])
        else:
            result += get_value(game[i+2])
    return result
