import pytest

from framework.factories.n_puzzle_config_generator import NPuzzleConfigGenerator
from framework.factories.n_queens_config_generator import NQueensConfigGenerator
from framework.factories.romania_config_generator import RomaniaConfigGenerator
from constants import ROMANIA_MAP

file_path = "tests/testfiles/"


def test_n_puzzle_creation():
    state = NPuzzleConfigGenerator.create(8, 1)
    state = state[0]
    state_length = len(state)
    all_differents = True
    all_in_range = True

    for i in range(state_length):
        for j in range(i + 1, state_length):
            if state[i] == state[j]:
                all_differents = False
        if state[i] < 0 or state[i] > state_length:
            all_in_range = False

    assert all_differents and all_in_range


def test_n_queens_creation():
    state = NQueensConfigGenerator.create(8, 1)
    state = state[0]
    state_length = len(state)
    all_in_range = True
    for i in range(state_length):
        if state[i] < -1 or state[i] >= state_length:
            all_in_range = False

    assert all_in_range


def test_romania_creation():
    state = RomaniaConfigGenerator.create(1)
    state = state[0]
    nodes = ROMANIA_MAP.nodes()
    all_in_map = True

    if not state[0] in nodes or not state[1] in nodes:
        all_in_map = False

    assert all_in_map


n_puzzle_file_configs = [
    (
        NPuzzleConfigGenerator.create_from_csv(file_path + "n_puzzle_creation.csv")[0],
        ("NPuzzle", (0, 6, 4, 1, 8, 7, 2, 5, 3)),
    ),
    (
        NPuzzleConfigGenerator.create_from_csv(file_path + "n_puzzle_creation.csv")[1],
        ("NPuzzle", (6, 0, 3, 8, 5, 4, 2, 1, 7)),
    ),
]


@pytest.mark.parametrize("file_state, expected_state", n_puzzle_file_configs)
def test_n_puzzle_right_creation_from_csv(file_state, expected_state):
    assert file_state == expected_state


n_queens_file_configs = [
    (
        NQueensConfigGenerator.create_from_csv(file_path + "n_queens_creation.csv")[0],
        ("NQueens", [3, 5, 1, 1, 3, 1]),
    ),
    (
        NQueensConfigGenerator.create_from_csv(file_path + "n_queens_creation.csv")[1],
        ("NQueens", [4, 1, 3, 2, 4, 1]),
    ),
]


@pytest.mark.parametrize("file_state, expected_state", n_queens_file_configs)
def test_n_queens_right_creation_from_csv(file_state, expected_state):
    assert file_state == expected_state


romania_file_configs = [
    (
        RomaniaConfigGenerator.create_from_csv(file_path + "romania_creation.csv")[0],
        ("Romania", ("Lugoj", "Giurgiu")),
    ),
    (
        RomaniaConfigGenerator.create_from_csv(file_path + "romania_creation.csv")[1],
        ("Romania", ("Craiova", "Rimnicu")),
    ),
]


@pytest.mark.parametrize("file_state, expected_state", n_queens_file_configs)
def test_romania_right_creation_from_csv(file_state, expected_state):
    print(file_state, expected_state)
    assert file_state == expected_state
