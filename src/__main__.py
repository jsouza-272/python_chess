from mypy.typeops import F

from .board import Board
from .consts import COORDS_TABLE
import os


board = Board()


user_input = ""
invalid_flag = False
movement = False
while user_input != "q":
    os.system("clear")
    print(board)
    if invalid_flag:
        invalid_flag = False
        print("invalid")
    user_input = input("q to quit: ")
    if user_input == "q":
        break
    if user_input == "m":
        movement = True
        user_input = input("piece coord:")
    if len(user_input) != 2:
        continue
    x, y = -1, -1
    for i, c in enumerate(user_input):
        if c not in COORDS_TABLE:
            break
        if i == 0:
            x = COORDS_TABLE[c]
        else:
            y = COORDS_TABLE[c]
    if x == -1 or y == -1:
        continue
    p_coord = (x, y)
    print(board[p_coord])
    possible_movements = board.possible_moves(p_coord)
    print(possible_movements)
    print(board.white_king.in_check)
    if movement:
        user_input = input("to: ")
        for i, c in enumerate(user_input):
            if c not in COORDS_TABLE:
                break
            if i == 0:
                x = COORDS_TABLE[c]
            else:
                y = COORDS_TABLE[c]
        if (x, y) not in possible_movements:
            invalid_flag = True
        board.move(p_coord, (x, y))
