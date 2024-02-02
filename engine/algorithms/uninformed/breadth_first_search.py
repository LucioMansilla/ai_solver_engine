from engine.algorithms.search_algorithm import SearchAlgorithm
from engine.data_structures.node import Node
from collections import deque
from engine.problems.problem import Problem


class BreadthFirstVisitedSearch(SearchAlgorithm):
    def search(self, problem: Problem) -> Node | None:
        frontier = deque([Node(problem.initial_state())])
        explored = set()
        while frontier:
            node = frontier.popleft()
            explored.add(node.state)
            if problem.goal_test(node.state):
                return node
            for child in node.expand(problem):
                if child.state not in explored and child not in frontier:
                    frontier.append(child)
        return None


class BreadthFirstSearch(SearchAlgorithm):
    def search(self, problem: Problem) -> Node | None:
        frontier = deque([Node(problem.initial_state())])  # FIFO queue
        while frontier:
            node = frontier.popleft()
            if problem.goal_test(node.state):
                return node
            frontier.extend(node.expand(problem))
        return None


class BreadthFirstAcyclicSearch(SearchAlgorithm):
    def search(self, problem: Problem) -> Node | None:
        frontier = deque([Node(problem.initial_state())])
        while frontier:
            node = frontier.popleft()
            if problem.goal_test(node.state):
                return node

            frontier.extend(
                child
                for child in node.expand(problem)
                if child not in frontier and child not in node.path()
            )
        return None
