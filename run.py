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
