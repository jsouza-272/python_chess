from abc import ABC, abstractmethod
from src.enums import Color
from src.aliases import Coord
from src.consts import BOARD_SIZE


class Piece(ABC):
    def __init__(self, color: Color, start_pos: Coord) -> None:
        super().__init__()
        self.__pos = start_pos
        self.color = color

    @property
    def pos(self) -> Coord:
        return self.__pos

    @pos.setter
    def pos(self, new: Coord) -> None:
        x, y = new
        if not (0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE):
            raise ValueError("Invalid coord")
        self.__pos = new

    def can_move(self, dest: Coord, board: list[list["Piece | None"]]) -> bool:
        dx, dy = dest
        if not (0 <= dx < BOARD_SIZE and 0 <= dy < BOARD_SIZE):
            return False
        dest_content = board[dy][dx]
        return self.can_eat(dest_content)

    @abstractmethod
    def possible_moves(self, board: list[list["Piece | None"]]) -> list[Coord]:
        ...

    @abstractmethod
    def can_eat(self, piece: "Piece | None") -> bool:
        ...
