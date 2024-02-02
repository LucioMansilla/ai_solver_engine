from engine.algorithms.search_algorithm import SearchAlgorithm
from engine.problems.problem import Problem
from engine.data_structures.node import Node
import random

class HillClimbingSearch(SearchAlgorithm):
    def __init__(self, heuristic):
        self.heuristic = heuristic

    def search(self, problem: Problem) -> Node | None:
        current = Node(problem.initial)
        while True:
            neighbors = current.expand(problem)
          
            if not neighbors:
                break
            neighbor = max(neighbors, key=lambda node: self.heuristic(node))
            if self.heuristic(neighbor) <= self.heuristic(current):
                return current
            current = neighbor
        return current


class HillClimbingSearchWithSidewaysMoves(SearchAlgorithm):
    def __init__(self, heuristic, sideways_moves=100):
        self.heuristic = heuristic
        self.sideways_moves = sideways_moves

    def search(self, problem: Problem) -> Node | None:
        current = Node(problem.initial_state())
        while True:
            neighbors = current.expand(problem)
          
          
            neighbor = max(neighbors, key=lambda node: self.heuristic(node))
            if self.heuristic(neighbor) < self.heuristic(current) or self.sideways_moves == 0 and self.heuristic(neighbor) == self.heuristic(current):
                return current
            
            if self.heuristic(neighbor) == self.heuristic(current):
                neighbor = random.choice([n for n in neighbors if self.heuristic(n) == self.heuristic(current)])
                self.sideways_moves -= 1

            else:
                self.sideways_moves = 100
            current = neighbor


class HillClimbingSearchWithRandomRestarts(SearchAlgorithm):
    def __init__(self, heuristic,restarts = 14):
        self.heuristic = heuristic
        self.restarts = restarts
        super().__init__()

    def search(self, problem: Problem) -> Node | None:
        state_factory = problem.factory()

        while self.restarts >= 0:
            problem.initial = state_factory.create()
            #problem.restart()
            node_hc :Node | None  = HillClimbingSearch(self.heuristic).search(problem)
            if node_hc is not None and problem.goal_test(node_hc.state):
                return node_hc
            self.restarts -= 1

        return None