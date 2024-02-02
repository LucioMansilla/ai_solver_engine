import random
from math import sqrt
from framework.filemanager.state_file_manager import StateFileManager
from constants import NPUZZLE


class NPuzzleConfigGenerator:

    @classmethod
    def create(cls, puzzle_number: int, amount: int) -> list[tuple]:
        states = []
        puzzle_number = int(sqrt(puzzle_number + 1))
        board = list(range(puzzle_number * puzzle_number))
        for _ in range(amount):
            new_state = cls.__generate_valid_config(board)
            states.append(new_state)
        return states

    @classmethod
    def create_from_csv(cls, file_path: str) -> list[tuple]:
        states = StateFileManager.create_from_csv(file_path)
        for state in states:
            problem_name = state[0]
            current_state = state[1]
            if problem_name != NPUZZLE:
                raise Exception(
                    f"Invalid problem name on input. Expected NPUZZLE but got {problem_name}"
                )
            if not cls.__is_valid_state(current_state):
                raise Exception(f"Invalid state on input. Got {current_state}")
        return states

    @classmethod
    def __generate_valid_config(cls, board: list) -> tuple:
        invalid_state = True
        while invalid_state:
            random.shuffle(board)
            if cls.__is_valid_state(board):
                invalid_state = False
        return tuple(board.copy())

    @classmethod
    def __is_valid_state(cls, ls: list) -> bool:
        inversion_counter = 0
        for i in range(len(ls) - 1):
            for j in range(i + 1, len(ls)):
                if ls[i] > ls[j] and ls[i] != 0 and ls[j] != 0:
                    inversion_counter = inversion_counter + 1
        return inversion_counter % 2 == 0
