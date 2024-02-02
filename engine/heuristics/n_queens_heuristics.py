from engine.data_structures.node import Node


def count_conflicted_queens(node: Node) -> int:
    num_conflicts = 0

    for r1, c1 in enumerate(node.state.data):
        for r2, c2 in enumerate(node.state.data):
            if (r1, c1) != (r2, c2):
                num_conflicts += check_conflict(r1, c1, r2, c2)

    return num_conflicts


def check_conflict(row1: int, col1: int, row2: int, col2: int) -> bool:
    return (
        row1 == row2
        or col1 == col2
        or row1 - col1 == row2 - col2  # same row
        or row1 + col1 == row2 + col2  # same \ diagonal
    )  # same / diagonal

def inverse_count_conflicted_queens(node: Node) -> int:
    return -count_conflicted_queens(node)