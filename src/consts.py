from .enums import PieceType


COORDS_TABLE = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "1": 0,
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7
    }

BOARD_SIZE = 8

WHITE_PAWN_DIRECTION = [(0, -1)]
BLACK_PAWN_DIRECTION = [(0, 1)]
ROOK_DIRECTION = [(-1, 0), (1, 0), (0, -1), (0, 1)]
BISHOP_DIRECTION = [(-1, -1), (1, 1), (-1, 1), (1, -1)]
KNIGHT_DIRECTION = [(-1, -2), (1, -2), (-2, 1), (-2, -1),
                    (2, 1), (2, -1), (1, 2), (-1, 2)]
QUEEN_DIRECTION = BISHOP_DIRECTION + ROOK_DIRECTION
KING_DIRECTION = BISHOP_DIRECTION + ROOK_DIRECTION
KING_CHECK_DIRECTION = ROOK_DIRECTION + BISHOP_DIRECTION + KNIGHT_DIRECTION

WHITE_PAWN_TAKE_DIRECTIONS = [(1, -1), (-1, -1)]
BLACK_PAWN_TAKE_DIRECTIONS = [(1, 1), (-1, 1)]

WHITE_START_POS = {
    PieceType.PAWN: [(c, 6) for c in range(BOARD_SIZE)],
    PieceType.ROOK: [(0, 7), (7, 7)],
    PieceType.BISHOP: [(2, 7), (5, 7)],
    PieceType.KNIGHT: [(1, 7), (6, 7)],
    PieceType.QUEEN: [(3, 7)],
    PieceType.KING: [(4, 7)]
}
BLACK_START_POS = {
    k: [(x, BOARD_SIZE - 1 - y) for x, y in v]
    for k, v in WHITE_START_POS.items()
}
