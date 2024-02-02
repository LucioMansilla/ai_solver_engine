from engine.algorithms.search_algorithm import SearchAlgorithm
from engine.problems.problem import Problem
from engine.data_structures.node import Node


class DepthLimitedSearch(SearchAlgorithm):
    def __init__(self, limit: int = 50):
        self.limit = limit

    def search(self, problem: Problem) -> Node:
        from constants import CUT_OFF

        frontier = [Node(problem.initial_state())]
        result = None
        while frontier:
            node = frontier.pop()
            if problem.goal_test(node.state):
                return node
            if node.depth > self.limit:
                result = CUT_OFF
            else:
                frontier.extend(child for child in node.expand(problem))

        return result
