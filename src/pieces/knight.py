from .base import Piece
from src.enums import Color
from src.aliases import Coord
from src.consts import KNIGHT_DIRECTION


class Knight(Piece):
    def __init__(self, color: Color, start_pos: Coord) -> None:
        super().__init__(color, start_pos)

    def __repr__(self) -> str:
        if self.color == Color.WHITE:
            return "♞"
        return "♘"

    def possible_moves(self, board: list[list[Piece | None]]) -> list[Coord]:
        moves = []
        cx, cy = self.pos
        for x, y in KNIGHT_DIRECTION:
            nx, ny = cx + x, cy + y
            if self.can_move((nx, ny), board):
                moves.append((nx, ny))
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
        return abs(diff_x) * abs(diff_y) == 2
