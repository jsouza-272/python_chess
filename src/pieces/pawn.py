from .base import Piece
from src.enums import Color
from src.aliases import Coord
from src.consts import (
    WHITE_PAWN_DIRECTION, BLACK_PAWN_DIRECTION,
    WHITE_PAWN_TAKE_DIRECTIONS, BLACK_PAWN_TAKE_DIRECTIONS
    )


class Pawn(Piece):
    def __init__(self, color: Color, start_pos: Coord) -> None:
        super().__init__(color, start_pos)
        self.first_move = True

    def __repr__(self) -> str:
        if self.color == Color.WHITE:
            return "♟"
        return "♙"

    def possible_moves(self, board: list[list[Piece | None]]) -> list[Coord]:
        moves = []
        directions = WHITE_PAWN_DIRECTION
        take_directions = WHITE_PAWN_TAKE_DIRECTIONS
        if self.color == Color.BLACK:
            directions = BLACK_PAWN_DIRECTION
            take_directions = BLACK_PAWN_TAKE_DIRECTIONS
        cx, cy = self.pos
        for x, y in take_directions:
            nx, ny = cx + x, cy + y
            if self.can_move((nx, ny), board) and board[ny][nx]:
                moves.append((nx, ny))
        dx, dy = directions[0]
        nx, ny = cx + dx, dy + cy
        if self.can_move((nx, ny), board) and not board[ny][nx]:
            moves.append((nx, ny))
        if self.first_move and not board[ny][nx]:
            self.first_move = False
            nx, ny = nx + dx, ny + dy
            if self.can_move((nx, ny), board) and not board[ny][nx]:
                moves.append((nx, ny))
        return moves

    def can_eat(self, piece: Piece | None) -> bool:
        if piece is None:
            return True
        if piece.color == self.color:
            return False
        take_directions = -1
        if self.color == Color.BLACK:
            take_directions = 1
        px, py = piece.pos
        cx, cy = self.pos
        diff_x = px - cx
        diff_y = py - cy
        return abs(diff_x) == 1 and diff_y == take_directions
