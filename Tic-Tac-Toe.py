def winner(x, y):
    flag = False
    if (x[0] == x[1] == x[2] and x[1] == y \
    or x[3] == x[4] == x[5] and x[4] == y \
    or x[6] == x[7] == x[8] and x[7] == y \

    or x[0] == x[3] == x[6] and x[3] == y \
    or x[1] == x[4] == x[7] and x[4] == y \
    or x[2] == x[5] == x[8] and x[5] == y \

    or x[0] == x[4] == x[8] and x[4] == y \
    or x[2] == x[4] == x[6] and x[4] == y):
        
        flag = True
    return flag

def status(x):
    if (winner(x, 'X') == True and winner(x, 'O') == True) or abs(x.count('O') - x.count('X')) > 1:
        return 'Impossible'
    elif winner(x, 'X') == True:
        return 'X wins'
    elif winner(x, 'O') == True:    
        return 'O wins'
    elif ' ' in x:
        return 'Game not finished'
    else:
        return 'Draw'
    
    

def game_act(xls, face):
    flag = 0
    while flag == 0:
        n = input('Enter the coordinates: ')

        if n.replace(' ', '').isnumeric() == False or len(n.split()) < 2:
            print('You should enter numbers!')


        elif n.split()[0] not in ['1','2','3'] or n.split()[1] not in ['1','2','3']:
            print('Coordinates should be from 1 to 3!')


        else:
            r, c = [int(i) for i in n.split()]

            if r == 1 and c == 1 and xls[0] == ' ':
                xls[0] = face
                flag = 1
            elif r == 1 and c == 2 and xls[1] == ' ':
                xls[1] = face
                flag = 1
            elif r == 1 and c == 3 and xls[2] == ' ':
                xls[2] = face
                flag = 1
            elif r == 2 and c == 1 and xls[3] == ' ':
                xls[3] = face
                flag = 1
            elif r == 2 and c == 2 and xls[4] == ' ':
                xls[4] = face
                flag = 1
            elif r == 2 and c == 3 and xls[5] == ' ':
                xls[5] = face
                flag = 1
            elif r == 3 and c == 1 and xls[6] == ' ':
                xls[6] = face
                flag = 1
            elif r == 3 and c == 2 and xls[7] == ' ':
                xls[7] = face
                flag = 1
            elif r == 3 and c == 3 and xls[8] == ' ':
                xls[8] = face
                flag = 1
            else:
                print('This cell is occupied! Choose another one!')


    if flag == 1: 
        print('---------')
        ls = []  
        for i in ''.join(xls):
            ls.append(i)
            if len(ls) > 2:
                print('|', *ls, '|')
                ls = []
        print('---------')
        
def game():
    x = '_________'.replace('_', ' ')
    ls = []
    print('---------')
    for i in x:
        ls.append(i)
        if len(ls) > 2:
            print('|', *ls, '|')
            ls = []    
    print('---------')
    xls = list(x)

    face = 0

    while status(xls) == 'Game not finished':
        if face % 2 == 0:
            game_act(xls, 'X')
            face += 1
        else:
            game_act(xls, 'O')
            face += 1
    else:
        print(status(xls))

