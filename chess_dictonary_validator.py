
"""
Chess Dictionary Validator
In this chapter, we used the dictionary value {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'} to represent a chess board.

Write a function named isValidChessBoard() that takes a dictionary argument and returns True or False depending on if the board is valid.

- A valid board will have exactly one black king and exactly one white king.
- Each player can only have at most 16 pieces, at most 8 pawns, and all pieces must be on a valid space from '1a' to '8h'; that is, a piece can’t be on space '9z'.
- The piece names begin with either a 'w' or 'b' to represent white or black, followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'.
- This function should detect when a bug has resulted in an improper chess board.
"""

def isValidChessBoard(board: dict):
    
    colors = ['b', 'w']
    
    valid_count = {'king': (1, 1),
                    'queen': (0, 1),
                    'rook': (0, 2),
                    'bishop': (0, 2),
                    'knight': (0, 2),
                    'pawn': (0, 8)
                    }

 
    # check location:
    for key in board.keys():
        if int(key[0]) not in range(1, 9) or key[1] not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
            return False

    
    # check names:
    for value in board.values():
        if value[0] not in colors or value[1:] not in valid_count.keys():
            return False

    # check number of pieces:
    counts = {}

    for value in board.values():
        if value not in counts.keys():
            counts[value] = 1
        else:
            counts[value] += 1

    for key, value in counts.items():
        if value < valid_count[key[1:]][0]:
            return False
        if value > valid_count[key[1:]][1]:
            return False

    return True

board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(isValidChessBoard(board))
