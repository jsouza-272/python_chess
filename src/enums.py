from enum import Enum


class Color(Enum):
    WHITE = 1
    BLACK = 2


class PieceType(Enum):
    PAWN = 1
    KING = 2
    BISHOP = 3
    KNIGHT = 4
    QUEEN = 5
    ROOK = 6
