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
from engine.problems.n_puzzle import NPuzzleProblem, NPuzzleState
from engine.problems.n_queens import NQueenState, NQueensProblem
from engine.problems.problem import StatisticsProblemDecorator
from engine.problems.romania import RomaniaProblem, RomaniaState
from engine.problems.problem import Problem


class ProblemFactory:
    PROBLEM = 0

    @classmethod
    def create(cls, params: list) -> tuple[Problem, callable]:
        problem_name = params[cls.PROBLEM]
        if problem_name == NPUZZLE:
            initial_state_data = params[1]
            problem = StatisticsProblemDecorator(
                NPuzzleProblem(NPuzzleState(initial_state_data))
            )
            return problem, NPuzzleHeuristicFactory, #NPuzzleStateFactory..
        elif problem_name == NQUEENS:
            initial_state_data = params[1]
            problem = StatisticsProblemDecorator(
                NQueensProblem(NQueenState(initial_state_data))
            )
            return problem, NQueensHeuristicFactory
        elif problem_name == ROMANIA:
            origin, destination = params[1]
            problem = StatisticsProblemDecorator(
                RomaniaProblem(RomaniaState((origin, destination)))
            )
            return problem, RomaniaHeuristicFactory

        else:
            raise Exception("Problem not found")
