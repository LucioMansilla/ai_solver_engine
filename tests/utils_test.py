from constants import NPUZZLE, NQUEENS, ROMANIA
from engine.factories.heuristic_factories.n_puzzle_heuristic_factory import (
    NPuzzleHeuristicFactory,
)
from engine.factories.heuristic_factories.n_queens_heuristic_factory import (
    NQueensHeuristicFactory,
)
from engine.factories.heuristic_factories.romania_heuristic_factory import (
    RomaniaHeuristicFactory,
)


class UtilsTest:
    def convert_name_function(self, name):
        function_name = name.__name__
        return function_name.title().replace("_", "")

    def algorithm_name(self, algorithm):
        if algorithm.__class__.__name__ == "AStarSearch":
            return "A*"
        return algorithm.__class__.__name__

    def search_heuristic(self, problem_name: str, heuristic_name: str):
        if problem_name == NPUZZLE:
            return NPuzzleHeuristicFactory.create(heuristic_name)
        elif problem_name == NQUEENS:
            return NQueensHeuristicFactory.create(heuristic_name)
        elif problem_name == ROMANIA:
            return RomaniaHeuristicFactory.create(heuristic_name)

    

utils_test = UtilsTest()
