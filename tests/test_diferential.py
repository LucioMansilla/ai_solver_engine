import random
import pytest
from pytest import mark

from engine.algorithms.uninformed.iterative_deepening import IterativeDeepening
from engine.algorithms.uninformed.uniform_cost_search import UniformCostSearch
from tests.aima.search import uniform_cost_search as aima_uniform_cost_search
from tests.aima.search import (
    iterative_deepening_search as aima_iterative_deepening_search,
)
from tests.aima.search import astar_search as aima_astar_search
from tests.aima.search import best_first_graph_search as aima_best_first_search
from tests.aima.search import breadth_first_tree_search as aima_breadth_first_search
from tests.aima.search import (
    breadth_first_graph_search as aima_breadth_first_visited_search,
)
from tests.aima.search import (
    depth_first_graph_search as aima_depth_first_visited_search,
)
from tests.aima.search import hill_climbing as aima_hill_climbing


random.seed("aima-python")

from engine.problems.problem import StatisticsProblemDecorator
from engine.algorithms.informed.astar_search import AStarSearch
from engine.algorithms.informed.greedy_best_first_search import GreedyBestFirstSearch
from engine.algorithms.uninformed.breadth_first_search import BreadthFirstSearch
from engine.algorithms.uninformed.breadth_first_search import BreadthFirstVisitedSearch
from engine.algorithms.uninformed.depth_first_search import DepthFirstVisitedSearch
from engine.algorithms.local.hill_climbing import HillClimbingSearch
from engine.data_structures.node import Node
from engine.problems.n_puzzle import NPuzzleProblem, NPuzzleState
from engine.problems.n_queens import NQueensProblem, NQueenState
from engine.problems.romania import RomaniaProblem, RomaniaState
from engine.problems.problem import StatisticsProblemDecorator


from tests.utils_test import utils_test

initial = {
    "NPuzzle": StatisticsProblemDecorator(
        NPuzzleProblem((NPuzzleState((1, 2, 3, 4, 5, 6, 7, 8, 0))))
    ),
    "NQueens": StatisticsProblemDecorator(NQueensProblem(NQueenState([2, 1, 0, 1]))),
    "Romania": StatisticsProblemDecorator(
        RomaniaProblem(RomaniaState(("Arad", "Bucharest")))
    ),
}


informed_config = [
    (
        AStarSearch,
        aima_astar_search,
        utils_test.search_heuristic("NPuzzle", "Manhattan"),
        initial["NPuzzle"],
    ),
    (
        GreedyBestFirstSearch,
        aima_best_first_search,
        utils_test.search_heuristic("NPuzzle", "Manhattan"),
        initial["NPuzzle"],
    ),
    (
        AStarSearch,
        aima_astar_search,
        utils_test.search_heuristic("NQueens", "CountConflictedQueens"),
        initial["NQueens"],
    ),
    (
        GreedyBestFirstSearch,
        aima_best_first_search,
        utils_test.search_heuristic("NQueens", "CountConflictedQueens"),
        initial["NQueens"],
    ),
    (
        AStarSearch,
        aima_astar_search,
        utils_test.search_heuristic("Romania", "EuclideanDistance"),
        initial["Romania"],
    ),
    (
        GreedyBestFirstSearch,
        aima_best_first_search,
        utils_test.search_heuristic("Romania", "EuclideanDistance"),
        initial["Romania"],
    ),
]


@mark.parametrize("my_algorithm, aima_algorithm, heuristic, problem", informed_config)
def test_informed_algorithms(my_algorithm, aima_algorithm, heuristic, problem):
    my_solution: Node = my_algorithm(heuristic).search(problem)
    aima_solution: Node = aima_algorithm(problem, heuristic)
    assert my_solution.solution() == aima_solution.solution()


uninformed_config = [
    (UniformCostSearch, aima_uniform_cost_search, initial["NPuzzle"]),
    (IterativeDeepening, aima_iterative_deepening_search, initial["NPuzzle"]),
    (UniformCostSearch, aima_uniform_cost_search, initial["NQueens"]),
    (IterativeDeepening, aima_iterative_deepening_search, initial["NQueens"]),
    (UniformCostSearch, aima_uniform_cost_search, initial["Romania"]),
    (IterativeDeepening, aima_iterative_deepening_search, initial["Romania"]),
    (BreadthFirstSearch, aima_breadth_first_search, initial["NPuzzle"]),
    (BreadthFirstVisitedSearch, aima_breadth_first_visited_search, initial["NPuzzle"]),
    (DepthFirstVisitedSearch, aima_depth_first_visited_search, initial["NPuzzle"]),
    (BreadthFirstSearch, aima_breadth_first_search, initial["NQueens"]),
    (BreadthFirstVisitedSearch, aima_breadth_first_visited_search, initial["NQueens"]),
    (DepthFirstVisitedSearch, aima_depth_first_visited_search, initial["NQueens"]),
    (BreadthFirstSearch, aima_breadth_first_search, initial["Romania"]),
    (BreadthFirstVisitedSearch, aima_breadth_first_visited_search, initial["Romania"]),
    (DepthFirstVisitedSearch, aima_depth_first_visited_search, initial["Romania"]),
]


@pytest.mark.parametrize("my_algorithm, aima_algorithm, problem", uninformed_config)
def test_uninformed_algorithms(my_algorithm, aima_algorithm, problem):
    my_solution: Node = my_algorithm().search(problem)
    aima_solution: Node = aima_algorithm(problem)
    assert (
        my_solution.depth == aima_solution.depth
        and my_solution.state == aima_solution.state
        and my_solution.path_cost == aima_solution.path_cost
    )



def test_hill_climbing():
    from framework.factories.n_queens_config_generator import NQueensConfigGenerator
    from engine.algorithms.local.hill_climbing import HillClimbingSearch,HillClimbingSearchWithSidewaysMoves
    from engine.heuristics.n_queens_heuristics import inverse_count_conflicted_queens
    from engine.problems.n_queens import NQueenState, NQueensProblem,NQueensProblemBrute

    queens_states = NQueensConfigGenerator

    hill_climbing_config = NQueensConfigGenerator.create(8, 100)
    count_goals = 0
    for current_state in hill_climbing_config:
        problem = NQueensProblemBrute(NQueenState(current_state))
        algorithm = HillClimbingSearch(inverse_count_conflicted_queens)
        solution = algorithm.search(problem)
        if solution.state.is_goal():
            count_goals += 1
    assert count_goals >= 5

def test_hill_climbing_sideways():
    from framework.factories.n_queens_config_generator import NQueensConfigGenerator
    from engine.algorithms.local.hill_climbing import HillClimbingSearch,HillClimbingSearchWithSidewaysMoves
    from engine.heuristics.n_queens_heuristics import inverse_count_conflicted_queens
    from engine.problems.n_queens import NQueenState, NQueensProblem,NQueensProblemBrute

    queens_states = NQueensConfigGenerator

    hill_climbing_config = NQueensConfigGenerator.create(8, 50)
    count_goals = 0
    for current_state in hill_climbing_config:
        problem = NQueensProblemBrute(NQueenState(current_state))
        algorithm = HillClimbingSearchWithSidewaysMoves(inverse_count_conflicted_queens)
        solution = algorithm.search(problem)
        if solution.state.is_goal():
            count_goals += 1
    assert count_goals >= 25
 

def test_hill_climbing_with_restarts():
    from framework.factories.n_queens_config_generator import NQueensConfigGenerator
    from engine.algorithms.local.hill_climbing import HillClimbingSearchWithRandomRestarts
    from engine.heuristics.n_queens_heuristics import inverse_count_conflicted_queens
    from engine.problems.n_queens import NQueenState, NQueensProblem,NQueensProblemBrute

    queens_states = NQueensConfigGenerator

    hill_climbing_config = NQueensConfigGenerator.create(8, 50)
    count_goals = 0
    for current_state in hill_climbing_config:
        problem = NQueensProblemBrute(NQueenState(current_state))
        algorithm = HillClimbingSearchWithRandomRestarts(inverse_count_conflicted_queens)
        solution = algorithm.search(problem)
        if solution and solution.state.is_goal():
            count_goals += 1
    assert count_goals >= 20 #p >= 50% 
    
    
    

