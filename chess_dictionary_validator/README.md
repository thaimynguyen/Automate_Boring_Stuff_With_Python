## Automate the Boring Stuff with Python by AL Sweigart
## Chapter 5: DICTIONARIES AND STRUCTURING DATA
### Ebook link: https://automatetheboringstuff.com/2e/chapter5/#calibre_link-204

Using the dictionary value, for example {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'} to represent a chess board, write a function named *isValidChessBoard()* that takes a dictionary argument and returns True or False depending on if the board is valid.

- A valid board will have exactly one black king and exactly one white king.
- Each player can only have at most 16 pieces, at most 8 pawns, and all pieces must be on a valid space from '1a' to '8h'; that is, a piece can’t be on space '9z'.
- The piece names begin with either a 'w' or 'b' to represent white or black, followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'.
- This function should detect when a bug has resulted in an improper chess board.


![The coordinates of a chessboard in algebraic chess notation](https://automatetheboringstuff.com/2e/images/000006.jpg)

The coordinates of a chessboard in algebraic chess notation



