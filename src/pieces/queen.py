from .base import Piece
from src.enums import Color
from src.aliases import Coord
from src.consts import QUEEN_DIRECTION


class Queen(Piece):
    def __init__(self, color: Color, start_pos: Coord) -> None:
        super().__init__(color, start_pos)

    def __repr__(self) -> str:
        if self.color == Color.WHITE:
            return "♛"
        return "♕"

    def possible_moves(self, board: list[list[Piece | None]]) -> list[Coord]:
        moves = []
        cx, cy = self.pos
        for x, y in QUEEN_DIRECTION:
            nx, ny = cx + x, cy + y
            while self.can_move((nx, ny), board):
                moves.append((nx, ny))
                if board[ny][nx] is not None:
                    break
                nx, ny = nx + x, ny + y
        return moves

    def can_eat(self, piece: Piece | None) -> bool:
        if piece is None:
            return True
        if piece.color == self.color:
            return False
        px, py = piece.pos
        cx, cy = self.pos
        diff_x = px - cx
        diff_y = py - cy
        return ((diff_x == 0) ^ (diff_y == 0)
                or diff_x != 0 and abs(diff_x) == abs(diff_y))
