from engine.data_structures.node import Node


def sum_weighted(node: Node) -> int:
    items = node.state.data
    weights = node.state.weights
    accum = 0
    values = node.state.values
    capacity = node.state.capacity
    for i in range(len(items)):
        if items[i] == 1:
            accum += values[i]
            capacity -= weights[i]
        if capacity < 0:
            return -1
    return accum
