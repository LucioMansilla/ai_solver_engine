import pytest
from constants import *
from engine.problems.knapsack import KnapSackProblem, KnapsackState,PutInKnapSack


# -- Test KnapsackState --#

is_goal_config = [
    (KnapsackState([0, 0, 0], [1, 2, 3], 5, [1, 2, 3]), False),
    (KnapsackState([0, 0, 0], [1, 2, 3], 5, [1, 2, 3]), False),
    (KnapsackState([0, 0, 0], [1, 2, 3], 5, [1, 2, 3]), False),
]
@pytest.mark.parametrize("current_state, expected_result", is_goal_config)
def test_is_goal(current_state, expected_result):
    assert current_state.is_goal() == expected_result


sum_sack_value_config = [
    (KnapsackState([0, 0, 0], [1, 2, 3], 5, [1, 2, 3]), 0),
    (KnapsackState([1, 0, 0], [1, 2, 3], 5, [1, 2, 3]), 1),
    (KnapsackState([1, 1, 0], [1, 2, 3], 5, [1, 2, 3]), 3),
    (KnapsackState([1, 1, 1], [1, 2, 3], 5, [1, 2, 3]), 6),
]
@pytest.mark.parametrize("current_state, expected_result", sum_sack_value_config)
def test_sum_sack_value(current_state, expected_result):
    assert current_state.sack_value == expected_result


sum_sack_weight_config = [
    (KnapsackState([0, 0, 0], [1, 2, 3], 5, [1, 2, 3]), 0),
    (KnapsackState([1, 0, 0], [1, 2, 3], 5, [1, 2, 3]), 1),
    (KnapsackState([1, 1, 0], [1, 2, 3], 5, [1, 2, 3]), 3),
    (KnapsackState([1, 1, 1], [1, 2, 3], 5, [1, 2, 3]), 6),
    (KnapsackState([1, 1, 1], [1, 2, 5], 5, [1, 2, 3]), 8),
    (KnapsackState([1, 0, 1], [1, 2, 5], 5, [1, 2, 3]), 6),
]
@pytest.mark.parametrize("current_state, expected_result", sum_sack_weight_config)
def test_sum_sack_weight(current_state, expected_result):
    assert current_state.sack_weight == expected_result


# -- Test KnapsackActions --#
is_enabled_actions_config = [
    (KnapSackProblem(KnapsackState([0, 0, 0], [1, 2, 3], 5, [1, 2, 3])), (PutInKnapSack(0), PutInKnapSack(1), PutInKnapSack(2))),
    (KnapSackProblem(KnapsackState([1, 0, 0], [1, 2, 3], 5, [1, 2, 3])), (PutInKnapSack(1), PutInKnapSack(2))),
    (KnapSackProblem(KnapsackState([1, 1, 0], [1, 2, 3], 5, [1, 2, 3])), (PutInKnapSack(2),)),
    (KnapSackProblem(KnapsackState([1, 1, 1], [1, 2, 3], 5, [1, 2, 3])), ()),
]
@pytest.mark.parametrize("problem, expected_result", is_enabled_actions_config)
def test_is_enabled_actions(problem, expected_result):
    list_actions = problem.actions(problem.initial)
    for a in list_actions:
        assert a in expected_result
    