from framework.factories.n_puzzle_config_generator import NPuzzleConfigGenerator
from framework.factories.n_queens_config_generator import NQueensConfigGenerator
from framework.factories.romania_config_generator import RomaniaConfigGenerator
from constants import NPUZZLE, NQUEENS, ROMANIA


class StateFactory:
    @classmethod
    def create(cls, problem: str, amount: int) -> list[tuple]:
        states = []
        if problem[0] == NPUZZLE:
            puzzle_number = int(problem[1])
            states = NPuzzleConfigGenerator(puzzle_number,amount).create()

        elif problem[0] == NQUEENS:
            queens_number = int(problem[1])
            states = NQueensConfigGenerator.create(queens_number, amount)

        elif problem[0] == ROMANIA:
            states = RomaniaConfigGenerator.create(amount)

        return states

    @classmethod
    def create_from_csv(cls, problem_name: str, file_path: str) -> list:
        if problem_name == NPUZZLE:
            return NPuzzleConfigGenerator.create_from_csv(file_path)

        if problem_name == NQUEENS:
            return NQueensConfigGenerator.create_from_csv(file_path)

        if problem_name == ROMANIA:
            return RomaniaConfigGenerator.create_from_csv(file_path)
        else:
            raise Exception("Problem not found")
