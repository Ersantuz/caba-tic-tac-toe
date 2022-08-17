from termcolor import colored
from time import sleep
import numpy as np
import random

# Initialize game field values
game_keys = np.array([['q', 'w', 'e'],
                      ['a', 's', 'd'],
                      ['z', 'x', 'c']])

# Detect all possible win combinations
win_keys_combinations = np.array([game_keys[:, 0],
                                  game_keys[:, 1],
                                  game_keys[:, 2],
                                  game_keys[0, :],
                                  game_keys[1, :],
                                  game_keys[2, :],
                                  np.array([game_keys[0, 0],
                                            game_keys[1, 1],
                                            game_keys[2, 2]]),
                                  np.array([game_keys[0, 2],
                                            game_keys[1, 1],
                                            game_keys[2, 0]])
                                  ])


# Render game field
def render_key(key):
    """
    Check if the value is None and manage print statement
    """
    if key is None:
        return ' '
    return key


def render_field(field):
    """
    Render the game field on the console
    """
    print('\n')
    print(render_key(field['q']) +
          ' | ' +
          render_key(field['w']) +
          ' | ' +
          render_key(field['e']))
    print('--+---+--')
    print(render_key(field['a']) +
          ' | ' +
          render_key(field['s']) +
          ' | ' +
          render_key(field['d']))
    print('--+---+--')
    print(render_key(field['z']) +
          ' | ' +
          render_key(field['x']) +
          ' | ' +
          render_key(field['c']))
    print('\n')


def status(matrix):
    """
    Create a vector representing the actual game status,
    where the status is described by the sum of the vector
    elements in the winning combinations.
    """
    res = np.zeros(8)
    res[0:3] = matrix.sum(axis=0)  # Columns combinations
    res[3:6] = matrix.sum(axis=1)  # Rows combinations
    res[6] = matrix.trace()  # Diagonal
    res[7] = np.flip(matrix, axis=1).trace()  # Anti-diagonal

    return res


def check_win(matrix):
    """
    Check if there is a winner
    """
    # Check game status
    res = status(matrix)

    # Check if there is a winner
    if np.any(res == 3):
        winner_combination = np.where(res == 3)[0]
        winner = 'X'
        win = True
        return win, winner, winner_combination
    elif np.any(res == -3):
        winner_combination = np.where(res == -3)[0]
        winner = 'O'
        win = True
        return win, winner, winner_combination
    else:
        winner_combination = None
        winner = None
        win = False
        return win, winner, winner_combination


def play(mod):
    ''' The game will be first initialized to create an empty
    game field, count the number of turns played and
    understand who is first to move. Then the game is played 
    until there is a winner or the game is a draw. At the end
    of the game the player can choose to play again or not.
    If played again, only the game field and the number of turn
    played will be reinitialized, while the first mover will be
    the who was not the first mover in the previous game.
    Finally the input mod will determine if the opponent is
    the computer or another player'''
    # Initialize game
    # Initialize first move
    global prev_first_move
    try:
        prev_first_move
    except NameError:
        prev_first_move = 'O'

    # Initialize game field
    game_field = {key: None for key in game_keys.flatten()}
    game_matrix = np.zeros((3, 3))

    turn = 0
    move = 'X' if prev_first_move == 'O' else 'O'

    print('\n' + move + ' starts, good luck!')

    # Start game
    while turn < 9:

        render_field(game_field)
        print(move + ' moves, select a key to place your move')

        # Get input
        if int(mod) == 1:
            entry = input()
        else:
            if move == 'X':
                entry = input()
            else:
                sleep(1.5)
                entry = computer_move(game_matrix)
                print(entry)

        # Check if the input is valid
        if entry in game_field.keys():
            if game_field[entry] is None:
                game_field[entry] = move
                turn += 1
            else:
                print('The entry selected is already filled, ' +
                      'choose a different cell')
                continue
        else:
            print('The entry selected is not valid, ' +
                  'choose a different key')
            continue

        # Update game matrix
        game_matrix = np.array([0 if move is None
                                else (1 if move == 'X' else -1)
                                for move in game_field.values()])
        game_matrix = game_matrix.reshape(3, 3)

        # Check if the game is over
        if turn > 2:
            win, winner, winner_combination = check_win(game_matrix)
            if win:
                break

        # Next move
        move = 'X' if move == 'O' else 'O'

    # End game
    if win:
        for key in win_keys_combinations[winner_combination][0]:
            game_field[key] = colored(game_field[key], 'red')
        render_field(game_field)
        print(colored('\nCongratulation ' + winner + ', you won!', 'green'))
    else:
        render_field(game_field)
        print(colored("\nGreat game, it's a tie!", 'yellow'))


print('-' * 50)
print('\nWelcome to tic-tac-toe (Cabaret edition)!\n')
print('-' * 50)
print('\nPlay with your friends and family or challenge our artificial ' +
      'intelligence (AI) Joep to see if machines are ready to defeat ' +
      'us!\n')
print('\nTic-tac-toe rules are simple and well defined, you can consult ' +
      'wikipedia(https://en.wikipedia.org/wiki/Tic-tac-toe) ' +
      'to refresh your mind.')
print('Specifically, to play on this platform you need to remember ' +
      'the following simple rules:')
print('\n1. The game is played on a grid that\'s 3 squares by 3. ' +
      'Each square is identified by a key and it can be represented as:')
print('\n  q | w | e ')
print('  --+---+--- ')
print('  a | s | d ')
print('  --+---+--- ')
print('  z | x | c \n')
print('  By entering the key showed in the figure above you can place ' +
      'your move on the corresponding square. Such keys are chosen ' +
      'for convenience on a "qwerty" keyboard.')
print('  If you are playing on a different keyboard, I\'m sorry :)\n')
print('\n2. You are X, your friend (or the computer) is O. ' +
      'Players take turns putting their marks in empty squares.')
print('\n3. Try to let Joep win sometimes, it will make him happy!')
print('\n Have fun!!!\n')
print('-' * 50)
print('\n Ⓒ Agree to Disagree 2022\n')

play(1)