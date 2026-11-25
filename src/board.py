from .aliases import Coord
from .errors.InternalErrors import InvalidPiece
from .enums import Color, PieceType
from .pieces import (
    Piece, King, Queen, Bishop,
    Rook, Pawn, Knight
    )
from .consts import (
    WHITE_START_POS, BLACK_START_POS, BOARD_SIZE
)


class Board:
    def __init__(self) -> None:
        self.white_king = King(
            Color.WHITE,
            WHITE_START_POS[PieceType.KING][-1]
            )
        self.black_king = King(
            Color.BLACK,
            BLACK_START_POS[PieceType.KING][-1]
            )
        self.board = self.__build_board()

    def __str__(self) -> str:
        board_rep = "  A B C D E F G H\n"
        for i, line in enumerate(self.board, start=1):
            board_rep += f"{i} "
            for _ in line:
                if _ is None:
                    board_rep += "□ "
                else:
                    board_rep += f"{_!r} "
            board_rep += "\n"
        return board_rep

    def __build_board(self) -> list[list[Piece | None]]:
        board: list[list[Piece | None]] = [
            [None for x in range(BOARD_SIZE)]
            for y in range(BOARD_SIZE)
            ]
        for k in WHITE_START_POS.keys():
            for x, y in WHITE_START_POS[k]:
                if k == PieceType.PAWN:
                    board[y][x] = Pawn(Color.WHITE, (x, y))
                elif k == PieceType.KING:
                    board[y][x] = self.white_king
                elif k == PieceType.QUEEN:
                    board[y][x] = Queen(Color.WHITE, (x, y))
                elif k == PieceType.ROOK:
                    board[y][x] = Rook(Color.WHITE, (x, y))
                elif k == PieceType.KNIGHT:
                    board[y][x] = Knight(Color.WHITE, (x, y))
                elif k == PieceType.BISHOP:
                    board[y][x] = Bishop(Color.WHITE, (x, y))
                else:
                    raise InvalidPiece(f"{k} not is a valid piece")
        for k in BLACK_START_POS.keys():
            for x, y in BLACK_START_POS[k]:
                if k == PieceType.PAWN:
                    board[y][x] = Pawn(Color.BLACK, (x, y))
                elif k == PieceType.KING:
                    board[y][x] = self.black_king
                elif k == PieceType.QUEEN:
                    board[y][x] = Queen(Color.BLACK, (x, y))
                elif k == PieceType.ROOK:
                    board[y][x] = Rook(Color.BLACK, (x, y))
                elif k == PieceType.KNIGHT:
                    board[y][x] = Knight(Color.BLACK, (x, y))
                elif k == PieceType.BISHOP:
                    board[y][x] = Bishop(Color.BLACK, (x, y))
                else:
                    raise InvalidPiece(f"{k} not is a valid piece")
        return board

    def __getitem__(self, key: Coord) -> Piece | None:
        x, y = key
        if not (0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE):
            return None
        return self.board[y][x]

    def reset_board(self) -> None:
        self.board = self.__build_board()
        self.white_king = King(
            Color.WHITE,
            WHITE_START_POS[PieceType.KING][-1]
            )
        self.black_king = King(
            Color.BLACK,
            BLACK_START_POS[PieceType.KING][-1]
            )

    def move(self, piece_coord: Coord, dest: Coord,
             simulate: bool = False) -> bool:
        px, py = piece_coord
        dx, dy = dest
        piece = self.board[py][px]
        print(piece)
        dest_content = self.board[dy][dx]
        if piece:
            self.board[py][px] = None
            self.board[dy][dx] = piece
            piece.pos = dest
            if piece.color == Color.WHITE:
                move = self.white_king.verify_check(
                    self.board, simulate=simulate
                    )
                if not simulate:
                    self.black_king.verify_check(self.board)
                if simulate:
                    self.board[py][px] = piece
                    self.board[dy][dx] = dest_content
                    piece.pos = piece_coord
                    return move
            elif piece.color == Color.BLACK:
                move = self.black_king.verify_check(
                    self.board, simulate=simulate
                    )
                if not simulate:
                    self.white_king.verify_check(self.board)
                if simulate:
                    self.board[py][px] = piece
                    self.board[dy][dx] = dest_content
                    piece.pos = piece_coord
                    return move
            return True
        return False

    def possible_moves(self, coord: Coord) -> list[Coord]:
        x, y = coord
        if not (0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE):
            return []
        content = self.board[y][x]
        if content is None:
            return []
        possible_moves = content.possible_moves(self.board)
        print(possible_moves)
        moves = []
        for movement in possible_moves:
            if self.move(coord, movement, simulate=True):
                moves.append(movement)
        return moves
