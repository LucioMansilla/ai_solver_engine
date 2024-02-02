import pytest

from constants import *
from engine.problems.n_puzzle import NPuzzleState, NPuzzleProblem
from engine.problems.n_puzzle import Up, Down, Left, Right

# -- Test NPuzzleState --#
idx_blank_square_config = [
    (NPuzzleState((1, 2, 3, 4, 5, 6, 7, 8, 0)), 8),
    (NPuzzleState((1, 2, 3, 4, 5, 6, 7, 0, 8)), 7),
    (NPuzzleState((1, 2, 3, 4, 5, 6, 0, 7, 8)), 6),
    (NPuzzleState((1, 2, 3, 4, 5, 0, 6, 7, 8)), 5),
    (NPuzzleState((1, 2, 3, 4, 0, 5, 6, 7, 8)), 4),
    (NPuzzleState((1, 2, 3, 0, 4, 5, 6, 7, 8)), 3),
    (NPuzzleState((1, 2, 0, 3, 4, 5, 6, 7, 8)), 2),
    (NPuzzleState((1, 0, 2, 3, 4, 5, 6, 7, 8)), 1),
    (NPuzzleState((0, 1, 2, 3, 4, 5, 6, 7, 8)), 0),
]


@pytest.mark.parametrize("current_state, expected_idx", idx_blank_square_config)
def test_idx_blank_square(current_state, expected_idx):
    assert current_state.get_index_blank_square() == expected_idx


position_blank_square_config = [
    (NPuzzleState((1, 2, 3, 4, 5, 6, 7, 8, 0)).is_blank_square_on_left_edge(), False),
    (NPuzzleState((1, 2, 3, 4, 5, 6, 7, 8, 0)).is_blank_square_on_right_edge(), True),
    (NPuzzleState((1, 2, 3, 4, 5, 6, 7, 8, 0)).is_blank_square_on_top_edge(), False),
    (NPuzzleState((1, 2, 3, 4, 5, 6, 7, 8, 0)).is_blank_square_on_bottom_edge(), True),
]


@pytest.mark.parametrize("current_state, expected_result", position_blank_square_config)
def test_position_blank_square(current_state, expected_result):
    assert current_state == expected_result


is_goal_config = [
    (NPuzzleState((1, 2, 3, 4, 5, 6, 7, 8, 0)), True),
    (NPuzzleState((1, 2, 3, 4, 5, 6, 7, 0, 8)), False),
    (NPuzzleState((1, 2, 3, 4, 5, 6, 0, 7, 8)), False),
]


@pytest.mark.parametrize("current_state, expected_result", is_goal_config)
def test_is_goal(current_state, expected_result):
    assert current_state.is_goal() == expected_result


is_valid_config = [
    (NPuzzleState((1, 2, 3, 4, 5, 6, 7, 8, 0)), True),
    (NPuzzleState((1, 2, 3, 4, 5, 6, 7, 0, 8)), True),
    (NPuzzleState((1, 2, 3, 4, 5, 6, 0, 7, 8)), True),
]


@pytest.mark.parametrize("current_state, expected_result", is_valid_config)
def test_is_valid(current_state, expected_result):
    assert current_state.is_valid() == expected_result


get_puzzle_number_config = [
    (NPuzzleState((1, 2, 3, 4, 5, 6, 7, 8, 0)), 8),
    (NPuzzleState((1, 2, 3, 0)), 3),
    (NPuzzleState((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0)), 15),
]


@pytest.mark.parametrize("current_state, expected_result", get_puzzle_number_config)
def test_get_puzzle_number(current_state, expected_result):
    assert current_state.get_puzzle_number() == expected_result


# -- Test NPuzzleAction --#

is_enabled_actions_config = [
    (NPuzzleProblem(NPuzzleState((1, 2, 3, 4, 5, 6, 7, 8, 0))), (Left(), Up())),
    (
        NPuzzleProblem(NPuzzleState((1, 2, 3, 4, 5, 6, 7, 0, 8))),
        (Left(), Up(), Right()),
    ),
    (
        NPuzzleProblem(NPuzzleState((1, 2, 3, 4, 5, 6, 0, 7, 8))),
        (Left(), Up(), Right()),
    ),
    (NPuzzleProblem(NPuzzleState((1, 2, 3, 4, 5, 0, 6, 7, 8))), (Left(), Up(), Down())),
    (
        NPuzzleProblem(NPuzzleState((1, 2, 3, 4, 0, 5, 6, 7, 8))),
        (Left(), Up(), Down(), Right()),
    ),
    (
        NPuzzleProblem(NPuzzleState((1, 2, 3, 0, 4, 5, 6, 7, 8))),
        (Up(), Down(), Right()),
    ),
    (NPuzzleProblem(NPuzzleState((1, 2, 0, 3, 4, 5, 6, 7, 8))), (Down(), Left())),
    (
        NPuzzleProblem(NPuzzleState((1, 0, 2, 3, 4, 5, 6, 7, 8))),
        (Left(), Down(), Right()),
    ),
    (NPuzzleProblem(NPuzzleState((0, 1, 2, 3, 4, 5, 6, 7, 8))), (Down(), Right())),
]


@pytest.mark.parametrize("current_state, expected_result", is_enabled_actions_config)
def test_is_enabled_actions(current_state, expected_result):
    list_actions = current_state.actions(current_state.initial)
    for a in list_actions:
        assert a in expected_result


execute_actions_config = [
    (
        NPuzzleState((1, 2, 3, 4, 5, 6, 7, 8, 0)),
        (Left(), Up()),
        NPuzzleState((1, 2, 3, 4, 0, 6, 7, 5, 8)),
    ),
]


@pytest.mark.parametrize(
    "current_state, action, expected_result", execute_actions_config
)
def test_execute_actions(current_state, action, expected_result):
    for a in action:
        current_state = a.execute(current_state)
    assert current_state == expected_result


# -- Test NPuzzleProblem --#

inverse_config = [
    (
        NPuzzleProblem(NPuzzleState((0, 1, 2, 3, 4, 5, 6, 7, 8))).inverse(),
        NPuzzleState((1, 2, 3, 4, 5, 6, 7, 8, 0)),
    ),
]


@pytest.mark.parametrize("current_state, expected_result", inverse_config)
def test_inverse(current_state, expected_result):
    assert current_state.initial == expected_result
