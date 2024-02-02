from engine.algorithms.search_algorithm import SearchAlgorithm
from engine.problems.problem import Problem
from engine.data_structures.node import Node


class DepthFirstSearch(SearchAlgorithm):
    def search(self, problem: Problem) -> Node | None:
        frontier = [Node(problem.initial_state())]
        while frontier:
            node = frontier.pop()
            if problem.goal_test(node.state):
                return node
            frontier.extend(node.expand(problem))
        return None


class DepthFirstVisitedSearch(SearchAlgorithm):
    def search(self, problem: Problem) -> Node | None:
        frontier = [Node(problem.initial_state())]
        explored = set()
        while frontier:
            node = frontier.pop()
            if problem.goal_test(node.state):
                return node
            explored.add(node.state)
            frontier.extend(
                child
                for child in node.expand(problem)
                if child.state not in explored and child not in frontier
            )
        return None


class DepthFirstAcyclicSearch(SearchAlgorithm):
    def search(self, problem: Problem) -> Node | None:
        frontier = [Node(problem.initial_state())]
        while frontier:
            node = frontier.pop()
            if problem.goal_test(node.state):
                return node
            frontier.extend(
                child
                for child in node.expand(problem)
                if child not in frontier and child not in node.path()
            )

        return None
