from engine.core.engine import Engine
import pytest
from constants import (
    INFORMED_ALGORITHMS,
    UNINFORMED_ALGORITHMS,
    HEURISTIC_FACTORIES,
    AVAILABLE_PROBLEMS,
    DUMMY,
    NPUZZLE,
    ROMANIA,
)
from tests.utils_test import utils_test

initial_state_informed = {
    "NPuzzle": (1, 8, 2, 0, 4, 3, 7, 6, 5),
    "NQueens": [4, 4, 3, 2, 1, 5, 6, 7],
    "Romania": ("Arad", "Bucharest"),
}

final_state_informed = {
    "NPuzzle": [(1, 2, 3, 4, 5, 6, 7, 8, 0)],
    "NQueens": [[4, 7, 3, 0, 2, 5, 1, 6], [1, 4, 6, 3, 0, 7, 5, 2]],
    "Romania": [("Bucharest", "Bucharest")],
}


def create_engine_config_informed():
    config_informed = []
    for problem_name in AVAILABLE_PROBLEMS:
        for algorithm_name in INFORMED_ALGORITHMS.keys():
            for heuristic_name in HEURISTIC_FACTORIES[problem_name].heuristics.keys():
                if heuristic_name != "NonHeuristic":
                    config_informed.append(
                        (
                            problem_name,
                            initial_state_informed[problem_name],
                            algorithm_name,
                            heuristic_name,
                            final_state_informed[problem_name],
                        )
                    )
    return config_informed


engine_config_informed = create_engine_config_informed()

initial_state_uninformed = {
    "NPuzzle": (1, 2, 0, 5, 6, 3, 4, 7, 8),
    "NQueens": [2, 0, 3, 2],
    "Romania": ("Drobeta", "Sibiu"),
}

final_state_uninformed = {
    "NPuzzle": [(1, 2, 3, 4, 5, 6, 7, 8, 0)],
    "NQueens": [[2, 0, 3, 1], [1, 3, 0, 2]],
    "Romania": [("Sibiu", "Sibiu")],
}


def create_engine_config_uninformed():
    config_uninformed = []
    for problem_name in AVAILABLE_PROBLEMS:
        for algorithm_name in UNINFORMED_ALGORITHMS.keys():
            if not algorithm_name in [
                "DepthFirstSearch",
                "DepthFirstVisitedSearch",
                "BidirectionalSearch",
            ]:
                config_uninformed.append(
                    (
                        problem_name,
                        initial_state_uninformed[problem_name],
                        algorithm_name,
                        final_state_uninformed[problem_name],
                    )
                )
    return config_uninformed


engine_config_uninformed = create_engine_config_uninformed()


@pytest.mark.parametrize(
    "problem_name,current_state,algorithm,heuristic,final_state", engine_config_informed
)
def test_engine_informed_algorithms(
    problem_name, current_state, algorithm, heuristic, final_state
):
    e = Engine([problem_name, current_state], algorithm, heuristic)
    solution = e.solve()
    assert solution.final_state in final_state


@pytest.mark.parametrize(
    "problem_name,current_state,algorithm,final_state", engine_config_uninformed
)
def test_engine_uninformed_algorithms(
    problem_name, current_state, algorithm, final_state
):
    e = Engine([problem_name, current_state], algorithm)
    solution = e.solve()
    assert solution.final_state in final_state


@pytest.mark.parametrize(
    "problem_name,current_state,algorithm,heuristic,final_state", engine_config_informed
)
def test_engine_informed(
    problem_name, current_state, algorithm, heuristic, final_state
):
    e = Engine([problem_name, current_state], algorithm, heuristic)
    engine_heuristc = utils_test.convert_name_function(e.heuristic)
    engine_algorithm = utils_test.algorithm_name(e.algorithm)
    assert str(e.problem) == problem_name
    assert engine_heuristc == heuristic
    assert engine_algorithm == algorithm


@pytest.mark.parametrize(
    "problem_name,current_state,algorithm,final_state", engine_config_uninformed
)
def test_engine_uninformed(problem_name, current_state, algorithm, final_state):
    e = Engine([problem_name, current_state], algorithm)
    engine_algorithm = utils_test.algorithm_name(e.algorithm)
    assert str(e.problem) == problem_name
    assert str(e.heuristic.__name__) == DUMMY
    assert engine_algorithm == algorithm


initial_state_bidirectional = {
    "NPuzzle": (1, 4, 7, 2, 0, 8, 3, 6, 5),
    "Romania": ("Drobeta", "Sibiu"),
}

final_state_bidirectional = {
    "NPuzzle": (1, 2, 3, 4, 5, 6, 7, 8, 0),
    "Romania": ("Sibiu", "Drobeta"),
}


def create_config_bidirectional_search():
    config_bidirectional = []
    for problem_name in [NPUZZLE, ROMANIA]:
        config_bidirectional.append(
            (
                problem_name,
                initial_state_bidirectional[problem_name],
                "BidirectionalSearch",
                final_state_bidirectional[problem_name],
            )
        )
    return config_bidirectional


config_bidirectional_search = create_config_bidirectional_search()


@pytest.mark.parametrize(
    "problem_name,current_state,algorithm,final_state", config_bidirectional_search
)
def test_engine_bidirectional_search(
    problem_name, current_state, algorithm, final_state
):
    e = Engine([problem_name, current_state], algorithm)
    solution = e.solve()
    assert solution.final_state == final_state
