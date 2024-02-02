from engine.data_structures.node import Node


def incorrect_placed_squares(node: Node) -> int:
    state: list[tuple] = node.state.data
    result = 0

    for i in range(len(state)):
        if state[i] == i + 1:
            result += 1

    return node.state.get_puzzle_number() - result


def create_idx_matrix(size: int) -> tuple:
    return tuple((i, j) for i in range(size) for j in range(size))


def manhattan(node: Node) -> int:
    state = node.state.data
    size = node.state.sqrt_n
    matrix_goal = create_idx_matrix(size)
    distance = 0
    for i in range(size):
        for j in range(size):
            if state[i * size + j] != 0:
                x_goal, y_goal = matrix_goal[state[i * size + j] - 1]
                x, y = i, j
                distance += abs(x - x_goal) + abs(y - y_goal)
    return distance


def gaschnig(node: Node) -> int:
    res = 0
    state = list(node.state.data)
    size = node.state.sqrt_n
    goal = [i for i in range(1, size**2)] + [0]
    while state != goal:
        idx_blank_square = state.index(0)
        if goal[idx_blank_square] != 0:
            correct_value = goal[idx_blank_square]
            idx_correct_value = state.index(correct_value)
            state[idx_correct_value], state[idx_blank_square] = (
                state[idx_blank_square],
                state[idx_correct_value],
            )
        else:
            for i in range(size * size):
                if goal[i] != state[i]:
                    state[i], state[idx_blank_square] = (
                        state[idx_blank_square],
                        state[i],
                    )
                    break
        res += 1
    return res


def euclidean_distance(node: Node) -> float:
    arr = node.state.data
    size = node.state.sqrt_n
    res = 0
    for i in range(size):
        for j in range(size):
            if arr[i * size + j] != 0:
                x = (arr[i * size + j] - 1) // size
                y = (arr[i * size + j] - 1) % size
                res += ((i - x) ** 2 + (j - y) ** 2) ** 0.5
    return res
