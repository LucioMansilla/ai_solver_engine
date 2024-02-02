from engine.data_structures.node import Node
from engine.algorithms.search_algorithm import SearchAlgorithm
from engine.data_structures.priority_queue import PriorityQueue
from typing import Callable
from engine.problems.problem import Problem

class GreedyBestFirstSearch(SearchAlgorithm):
    def __init__(self, heuristic: Callable[[Node], float]):
        self.heuristic = heuristic

    def search(self, problem: Problem) -> Node | None:
        node = self._search(problem)
        return node

    def _search(self, problem: Problem) -> Node | None:
        node: Node = Node(problem.initial_state())
        frontier = PriorityQueue("min", self.heuristic)
        frontier.append(node)
        reached = {}
        while frontier:
            node = frontier.pop()
            if problem.goal_test(node.state):
                return node

            if node.state in reached and node.path_cost > reached[node.state].path_cost:
                continue

            for child in node.expand(problem):
                s = child.state
                if s not in reached or child.path_cost < reached[s].path_cost:
                    reached[s] = child
                    frontier.append(child)
        return None
