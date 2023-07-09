def pattern_print(game_pattern):
    print('---------')
    print('|', game_pattern[0][0], game_pattern[0][1], game_pattern[0][2],
          '|', sep=' ')
    print('|', game_pattern[1][0], game_pattern[1][1], game_pattern[1][2],
          '|', sep=' ')
    print('|', game_pattern[2][0], game_pattern[2][1], game_pattern[2][2],
          '|', sep=' ')
    print('---------')


def check_draw(game_matrix):
    empty_spaces_count = 0
    for row in game_matrix:
        if '_' in row:
            empty_spaces_count += 1
    if (empty_spaces_count == 0
            and not check_o_win(game_matrix)
            and not check_x_win(game_matrix)):
        return True
    else:
        return False


def check_x_win(game_matrix):
    if (game_matrix[0].count('X') == 3
            or game_matrix[1].count('X') == 3
            or game_matrix[2].count('X') == 3
            or (game_matrix[0][0] == 'X'
                and game_matrix[1][0] == 'X'
                and game_matrix[2][0] == 'X')
            or (game_matrix[0][1] == 'X'
                and game_matrix[1][1] == 'X'
                and game_matrix[2][1] == 'X')
            or (game_matrix[0][2] == 'X'
                and game_matrix[1][2] == 'X'
                and game_matrix[2][2] == 'X')
            or (game_matrix[0][0] == 'X'
                and game_matrix[1][1] == 'X'
                and game_matrix[2][2] == 'X')
            or (game_matrix[0][2] == 'X'
                and game_matrix[1][1] == 'X'
                and game_matrix[2][0] == 'X')):
        return True
    else:
        return False


def check_o_win(game_matrix):
    if (game_matrix[0].count('O') == 3
            or game_matrix[1].count('O') == 3
            or game_matrix[2].count('O') == 3
            or (game_matrix[0][0] == 'O'
                and game_matrix[1][0] == 'O'
                and game_matrix[2][0] == 'O')
            or (game_matrix[0][1] == 'O'
                and game_matrix[1][1] == 'O'
                and game_matrix[2][1] == 'O')
            or (game_matrix[0][2] == 'O'
                and game_matrix[1][2] == 'O'
                and game_matrix[2][2] == 'O')
            or (game_matrix[0][0] == 'O'
                and game_matrix[1][1] == 'O'
                and game_matrix[2][2] == 'O')
            or (game_matrix[0][2] == 'O'
                and game_matrix[1][1] == 'O'
                and game_matrix[2][0] == 'O')):
        return True
    else:
        return False


pattern = ' ' * 9
pattern_matrix = [[pattern[0], pattern[1], pattern[2]],
                  [pattern[3], pattern[4], pattern[5]],
                  [pattern[6], pattern[7], pattern[8]]]
pattern_print(pattern_matrix)
turns = 1
move_sign = 'X'

while True:
    move = input()
    if not move.replace(' ', '').isdecimal():
        print('You should enter numbers!')
    else:
        line, column = move.split(' ')
        line = int(line)
        column = int(column)
        if line < 1 or line > 3 or column < 1 or column > 3:
            print('Coordinates should be from 1 to 3!')
        elif (pattern_matrix[line - 1][column - 1] == 'X'
              or pattern_matrix[line - 1][column - 1] == 'O'):
            print('This cell is occupied! Choose another one!')
        else:
            if turns % 2 != 0:
                move_sign = 'X'
            else:
                move_sign = 'O'
            pattern_matrix[line - 1][column - 1] = move_sign
            turns += 1
            pattern_print(pattern_matrix)
            if check_x_win(pattern_matrix):
                print('X wins')
                break
            elif check_o_win(pattern_matrix):
                print('O wins')
                break
            elif turns == 10 and check_draw(pattern_matrix):
                print('Draw')
                break

# check_game_state(pattern_matrix)
