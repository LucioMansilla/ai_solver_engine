from engine.algorithms.uninformed.depth_limited_search import DepthLimitedSearch
from engine.algorithms.search_algorithm import SearchAlgorithm
from engine.problems.problem import Problem
from engine.data_structures.node import Node


class IterativeDeepening(SearchAlgorithm):
    def search(self, problem: Problem) -> Node | None:
        from constants import CUT_OFF

        limit = 0
        while True:
            result = DepthLimitedSearch(limit).search(problem)
            if result != CUT_OFF:
                return result
            limit += 1
