from .base import Piece
from src.enums import Color
from src.aliases import Coord
from src.consts import (
    KING_DIRECTION, QUEEN_DIRECTION, KNIGHT_DIRECTION,
    BOARD_SIZE
    )


class King(Piece):
    def __init__(self, color: Color, start_pos: Coord) -> None:
        super().__init__(color, start_pos)
        self.in_check = False

    def __repr__(self) -> str:
        if self.color == Color.WHITE:
            return "♚"
        return "♔"

    def verify_check(self, board: list[list[Piece | None]],
                     dest: Coord | None = None,
                     simulate: bool = False) -> bool:
        dx, dy = self.pos
        if dest is not None:
            dx, dy = dest
        for x, y in KNIGHT_DIRECTION:
            nx, ny = dx + x, dy + y
            if not (0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE):
                continue
            square_content = board[ny][nx]
            if square_content is None:
                continue
            elif square_content.can_eat(self):
                if not simulate:
                    self.in_check = True
                return False
        for x, y in QUEEN_DIRECTION:
            nx, ny = dx + x, dy + y
            while (0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE):
                square_content = board[ny][nx]
                if square_content is None:
                    nx, ny = nx + x, ny + y
                elif square_content.can_eat(self):
                    if not simulate:
                        self.in_check = True
                    return False
                else:
                    break
        self.in_check = False
        return True

    def can_move(self, dest: Coord, board: list[list[Piece | None]]) -> bool:
        dx, dy = dest
        if not (0 <= dx < BOARD_SIZE and 0 <= dy < BOARD_SIZE):
            return False
        dest_content = board[dy][dx]
        if dest_content and dest_content.color == self.color:
            return False
        return self.verify_check(board, (dx, dy), simulate=True)

    def possible_moves(self, board: list[list[Piece | None]]) -> list[Coord]:
        moves = []
        cx, cy = self.pos
        for x, y in KING_DIRECTION:
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
        return max(abs(diff_x), abs(diff_y)) == 1
