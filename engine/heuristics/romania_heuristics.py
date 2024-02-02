from math import sqrt
from engine.data_structures.node import Node


def euclidean_distance(node: Node) -> float:
    from constants import ROMANIA_DISTANCES

    (x1, y1) = ROMANIA_DISTANCES[node.state.current_city]
    (x2, y2) = ROMANIA_DISTANCES[node.state.goal_city]
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
