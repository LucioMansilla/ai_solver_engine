import random
from framework.filemanager.state_file_manager import StateFileManager
from constants import NQUEENS


class NQueensStateFactory:

    def __init__(self, N: int):
        self.N = N
    
    def create(self):
        from engine.problems.n_queens import NQueenState
        return NQueenState(NQueensConfigGenerator.create(self.N, 1)[0])


class NQueensConfigGenerator:
    @classmethod
    def create(cls, queens_number: int, amount: int) -> list:
        states = []
        for i in range(amount):
            new_state = cls.__generate_valid_config(queens_number)
            states.append(new_state)
        return states

    @classmethod
    def create_from_csv(cls, file_path: str) -> list[tuple]:
        states = StateFileManager.create_from_csv(file_path)
        for state in states:
            problem_name = state[0]
            current_state = state[1]
            if problem_name != NQUEENS:
                raise Exception(
                    f"Invalid problem name on input. Expected NQUEENS but got {problem_name}"
                )
            if not cls.__is_valid_state(current_state):
                raise Exception(f"Invalid state on input. Got {current_state}")
        return states

    @classmethod
    def __generate_valid_config(cls, queens_number: int) -> list:
        return list(random.randint(0, queens_number - 1) for _ in range(queens_number))

    @classmethod
    def __is_valid_state(cls, ls: list) -> bool:
        for i in range(len(ls)):
            if ls[i] < 0 or ls[i] > len(ls):
                return False
        return True
