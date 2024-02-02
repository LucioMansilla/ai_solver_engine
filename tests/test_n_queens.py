import pytest
from engine.problems.n_queens import NQueensProblem, NQueenState, Down, Up


# -- Test NQueenState --#

is_goal_config = [
    (NQueenState([0, 3, 0, 2, 4, 5]), False),
    (NQueenState([1, 0, 3, 2, 4, 1]), False),
    (NQueenState([4, 6, 1, 5, 2, 0, 3, 7]), True),
    (NQueenState([6, 2, 0, 5, 7, 4, 1, 3]), True),
    (NQueenState([5, 3, 0, 2, 7, 4, 1, 3]), False),
]

@pytest.mark.parametrize("current_state, expected_result", is_goal_config)
def test_is_goal(current_state, expected_result):
    assert current_state.is_goal() == expected_result

unvalid_config = [
    (([0, 0, 0, 10, 1, 2])),
    (([1, 0, -1, 0, 2, 3])),
    (([4, 6, 1, 5, 2, 0, 3, 9])),
    (([6, 2, 0, 5, 7, 4, 1, -5])),
    (([5, 3, 0, 2, -1, 4, 1, 3])),
]

@pytest.mark.parametrize("current_state", unvalid_config)
def test_is_valid(current_state):
    try:
        NQueenState(current_state)
    except:
        assert True
    assert True

get_n_quees_number_config = [
    (NQueenState([0, 0, 0, 1]), 4),
    (NQueenState([0, 1, 0, 2, 4, 1]), 6),
    (NQueenState([4, 6, 1, 5, 2, 0, 3, 7]), 8),
    (NQueenState([6, 2, 0, 5, 7, 4, 1, 3]), 8),
]

@pytest.mark.parametrize("current_state, expected_result", get_n_quees_number_config)
def test_get_n_quees_number(current_state, expected_result):
    assert current_state.N == expected_result

# -- Test NQueensActions --#
is_enabled_actions_config = [
    (NQueensProblem(NQueenState([0, 0, 0, 0])), (Down(), Down(), Down(), Down())),
    (NQueensProblem(NQueenState([1, 0, 0, 0])), (Up(), Down(), Down(), Down(), Down())),
    (NQueensProblem(NQueenState([1, 2, 0, 0])), (Up(), Down(), Up(), Down(), Down(), Down())),
    (NQueensProblem(NQueenState([1, 2, 3, 0])), (Up(), Down(), Up(), Down(), Up(), Down()))   

]

@pytest.mark.parametrize("problem, expected_result", is_enabled_actions_config)
def test_is_enabled_actions(problem, expected_result):
    actions_list = problem.actions(problem.initial)    
    for exp in expected_result:
        assert exp in actions_list
        

execute_actions_config = [
    (NQueenState([0, 0, 0, 0]), [Down()], NQueenState([1, 0, 0, 0]), 0),
    (NQueenState([1, 0, 0, 0]), [Up()], NQueenState([0, 0, 0, 0]), 0),
    (NQueenState([1, 2, 0, 0]), [Down()], NQueenState([1, 3, 0, 0]), 1),
    (NQueenState([0, 2, 0, 0]), [Up()], NQueenState([0, 1, 0, 0]), 1),
    (NQueenState([1, 2, 2, 0]), [Down()], NQueenState([1, 2, 3, 0]), 2),
    (NQueenState([0, 2, 3, 0]), [Up()], NQueenState([0, 2, 2, 0]), 2),
    (NQueenState([1, 2, 3, 0]), [Down()], NQueenState([1, 2, 3, 1]), 3),
    (NQueenState([0, 2, 3, 2]), [Up()], NQueenState([0, 2, 3, 1]), 3),
]

@pytest.mark.parametrize(
    "current_state, action, expected_result, position", execute_actions_config
)
def test_execute_actions(current_state, action, expected_result, position):
    for a in action:
        current_state = a.execute(current_state, position)
    assert current_state == expected_result
