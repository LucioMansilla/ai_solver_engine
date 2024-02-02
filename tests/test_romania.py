import pytest
from engine.problems.romania import RomaniaProblem, RomaniaState, RomaniaAction

# -- Test RomaniaState --#


is_goal_config = [
    (RomaniaState(("Arad", "Bucharest")), True),
    (RomaniaState(("Arad", "Buenos Aires")), False),
    (RomaniaState(("Buenos Aires", "Bucharest")), False),
]


@pytest.mark.parametrize("state, expected", is_goal_config)
def test_romania_valid_states(state, expected):
    assert state.is_valid() == expected


is_valid_config = [
    (RomaniaState(("Arad", "Bucharest")), False),
    (RomaniaState(("Bucharest", "Arad")), False),
    (RomaniaState(("Bucharest", "Bucharest")), True),
    (RomaniaState(("Arad", "Arad")), True),
]


@pytest.mark.parametrize("state, expected", is_valid_config)
def test_romania_valid_states(state, expected):
    assert state.is_goal() == expected


# -- Test RomaniaAction --#

is_enabled_actions_config = [
    (
        RomaniaProblem(RomaniaState(("Arad", "Bucharest"))),
        (
            RomaniaAction("Arad", "Sibiu", 140),
            RomaniaAction("Arad", "Timisoara", 118),
            RomaniaAction("Arad", "Zerind", 75),
        ),
    ),
    (
        RomaniaProblem(RomaniaState(("Zerind", "Bucharest"))),
        (RomaniaAction("Zerind", "Arad", 75), RomaniaAction("Zerind", "Oradea", 71)),
    ),
    (
        RomaniaProblem(RomaniaState(("Urziceni", "Bucharest"))),
        (
            RomaniaAction("Urziceni", "Bucharest", 85),
            RomaniaAction("Urziceni", "Hirsova", 98),
            RomaniaAction("Urziceni", "Vaslui", 142),
        ),
    ),
    (
        RomaniaProblem(RomaniaState(("Bucharest", "Bucharest"))),
        (
            RomaniaAction("Bucharest", "Urziceni", 85),
            RomaniaAction("Bucharest", "Giurgiu", 90),
            RomaniaAction("Bucharest", "Pitesti", 101),
            RomaniaAction("Bucharest", "Fagaras", 211),
        ),
    ),
    (
        RomaniaProblem(RomaniaState(("Hirsova", "Bucharest"))),
        (
            RomaniaAction("Hirsova", "Eforie", 86),
            RomaniaAction("Hirsova", "Urziceni", 98),
        ),
    ),
]


@pytest.mark.parametrize("current_state, expected_result", is_enabled_actions_config)
def test_is_enabled_actions(current_state, expected_result):
    actions = current_state.actions(current_state.initial)
    action_is_expected = True
    for action in actions:
        if action not in expected_result:
            action_is_expected = False

    assert action_is_expected


execute_actions_config = [
    (
        RomaniaProblem(RomaniaState(("Arad", "Bucharest"))),
        RomaniaAction("Arad", "Sibiu", 140),
        RomaniaState(("Sibiu", "Bucharest")),
    ),
    (
        RomaniaProblem(RomaniaState(("Zerind", "Bucharest"))),
        RomaniaAction("Zerind", "Arad", 75),
        RomaniaState(("Arad", "Bucharest")),
    ),
    (
        RomaniaProblem(RomaniaState(("Urziceni", "Bucharest"))),
        RomaniaAction("Urziceni", "Bucharest", 85),
        RomaniaState(("Bucharest", "Bucharest")),
    ),
    (
        RomaniaProblem(RomaniaState(("Bucharest", "Bucharest"))),
        RomaniaAction("Bucharest", "Urziceni", 85),
        RomaniaState(("Urziceni", "Bucharest")),
    ),
    (
        RomaniaProblem(RomaniaState(("Hirsova", "Bucharest"))),
        RomaniaAction("Hirsova", "Eforie", 86),
        RomaniaState(("Eforie", "Bucharest")),
    ),
]


@pytest.mark.parametrize(
    "current_state, action, expected_result", execute_actions_config
)
def test_execute_actions(current_state, action, expected_result):
    new_state = action.execute(current_state.initial)
    assert new_state == expected_result


# -- Test RomaniaProblem --#

inverse_config = [
    (
        RomaniaProblem(RomaniaState(("Arad", "Bucharest"))),
        RomaniaState(("Bucharest", "Arad")),
    ),
    (
        RomaniaProblem(RomaniaState(("Zerind", "Bucharest"))),
        RomaniaState(("Bucharest", "Zerind")),
    ),
]


@pytest.mark.parametrize("current_state, expected_result", inverse_config)
def test_inverse(current_state, expected_result):
    inverse_state = current_state.inverse()
    assert inverse_state.initial == expected_result


actions_for_path_cost = [
    (
        RomaniaProblem(RomaniaState(("Arad", "Bucharest"))),
        RomaniaAction("Arad", "Sibiu", 140),
        140,
    ),
    (
        RomaniaProblem(RomaniaState(("Zerind", "Bucharest"))),
        RomaniaAction("Zerind", "Arad", 75),
        75,
    ),
    (
        RomaniaProblem(RomaniaState(("Urziceni", "Bucharest"))),
        RomaniaAction("Urziceni", "Bucharest", 85),
        85,
    ),
    (
        RomaniaProblem(RomaniaState(("Bucharest", "Bucharest"))),
        RomaniaAction("Bucharest", "Urziceni", 85),
        85,
    ),
    (
        RomaniaProblem(RomaniaState(("Hirsova", "Bucharest"))),
        RomaniaAction("Hirsova", "Eforie", 86),
        86,
    ),
]


@pytest.mark.parametrize(
    "initial_state, action, expected_result", actions_for_path_cost
)
def test_actions_for_path_cost(initial_state, action, expected_result):
    current_cost = initial_state.path_cost(0, action.origin, action, action.destination)
    assert current_cost == expected_result
