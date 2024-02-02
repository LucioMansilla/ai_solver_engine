from engine.data_structures.node import Node
from engine.problems.problem import Problem, StatisticsProblemDecorator
from engine.algorithms.search_algorithm import SearchAlgorithm
from typing import Callable
import sys
import textwrap


class Solution:
    def __init__(
        self,
        algorithm: SearchAlgorithm,
        problem: Problem,
        heuristic: Callable[[Node], float],
        params: list,
    ):
        self.initial_state = problem.initial_state().data
        self.algorithm = algorithm.__class__.__name__
        self.heuristic = heuristic.__name__
        self.problem_name = problem
        self.params = params

    def __eq__(self, other):
        return (
            self.final_state == other.final_state
            and self.initial_state == other.initial_state
            and self.algorithm == other.algorithm
            and self.heuristic == other.heuristic
        )

    def __hash__(self):
        return hash(self.final_state)


class StatisticalSolution(Solution):
    def __init__(
        self,
        node: Node,
        algorithm: SearchAlgorithm,
        run_time: float,
        problem: Problem,
        memory: float,
        heuristic: Callable[[Node], float],
        params: list,
    ):
        super().__init__(algorithm, problem, heuristic, params=params)
        self.path = [node.state.data for node in node.path()]
        self.path_cost = node.path_cost
        self.action_sequence = node.solution()
        self.depth = node.depth
        self.run_time = round(run_time, 4)
        self.memory = memory
        self.generated_nodes = problem.generated_nodes
        self.approx_memory_generated = sys.getsizeof(node) * self.generated_nodes
        self.average_branching_factor = round(problem.average_branching_factor(), 4)
        self.max_nodes_in_frontier = problem.max_nodes_in_frontier
        self.visited_ones = problem.visited_ones
        self.no_leaf_nodes = problem.no_leaf_nodes
        self.final_state = node.state.data

    def __repr__(self):
        return f"""\n
        ----------------------Algorithm: {self.algorithm} , Problem: {self.problem_name}----------------------
        Initial State: {self.initial_state}
        Final State: {self.final_state}
        Path: {textwrap.fill(str(self.path),width=180,initial_indent=' '*0,subsequent_indent=' '*15)}
        Path Cost: {self.path_cost}
        Action Sequence: {self.action_sequence}
        Heuristic: {self.heuristic}
        ------------------------------------
        Depth: {self.depth}
        Generated Nodes: {self.generated_nodes}
        Visited Nodes: {self.visited_ones}
        Branching Factor: {self.average_branching_factor}
        Max Nodes in Frontier: {self.max_nodes_in_frontier}
        No Leaf Nodes: {self.no_leaf_nodes}
        ------------------------------------
        Memory Occupied(TRACEMALLOC): {self.memory}
        Execution Time: {self.run_time}     
        Brute Memory Generated(Approx): {self.approx_memory_generated}        
        -------------------------------------------------------------------------------------------------
        """

    def name_action_sequence(self):
        return [action for action in self.action_sequence]
    def to_csv(self):
        return SolutionFileManager.write_to_csv(self)

    def __eq__(self, other):
        return (
            isinstance(other, Solution)
            and self.final_state == other.final_state
            and self.path == other.path
            and self.path_cost == other.path_cost
            and self.action_sequence == other.action_sequence
            and self.depth == other.depth
            and self.run_time == other.run_time
            and self.memory == other.memory
            and self.generated_nodes == other.generated_nodes
        )

    def __hash__(self):
        return hash(self.final_state)


class NonSolution(Solution):
    def __init__(
        self,
        node: Node,
        algorithm: SearchAlgorithm,
        problem: Problem,
        heuristic: Callable[[Node], float],
        run_time: float,
        memory: float,
        params: list,
    ):
        super().__init__(algorithm, problem, heuristic, params=params)
        self.path = "No Path"
        self.path_cost = "No Path Cost"
        self.action_sequence = "No Action Sequence"
        self.depth = node.depth
        self.run_time = run_time
        self.memory = memory
        self.generated_nodes = problem.generated_nodes
        self.approx_memory_generated = problem.approx_memory_generated
        self.average_branching_factor = problem.average_branching_factor()
        self.max_nodes_in_frontier = problem.max_nodes_in_frontier
        self.visited_ones = problem.visited_ones
        self.no_leaf_nodes = problem.no_leaf_nodes
        self.final_state = "Solution doesn't exists"

    def __repr__(self):
        return f"""\n
        SOLUTION DOESN'T EXISTS
        Algorithm: {self.algorithm} , Problem: {self.problem_name}
        Initial State: {self.initial_state}
        Final State: {self.final_state}
        Path: {self.path}
        Path Cost: {self.path_cost}
        Action Sequence: {self.action_sequence}
        Heuristic: {self.heuristic}
        ------------------------------------
        Depth: {self.depth}
        Generated Nodes: {self.generated_nodes}
        Visited Nodes: {self.visited_ones}
        Branching Factor: {self.average_branching_factor}
        Max Nodes in Frontier: {self.max_nodes_in_frontier}
        No Leaf Nodes: {self.no_leaf_nodes}
        ------------------------------------
        Memory (TRACEMALLOC): {self.memory}
        Execution Time: {self.run_time}     
        Brute Memory Generated(Approx): {self.approx_memory_generated}        
        
        SOLUTION DOESN'T EXISTS
        """

    def __eq__(self, other):
        return (
            isinstance(other, Solution)
            and self.final_state == other.final_state
            and self.path == other.path
            and self.path_cost == other.path_cost
            and self.action_sequence == other.action_sequence
            and self.depth == other.depth
            and self.run_time == other.run_time
            and self.memory == other.memory
            and self.generated_nodes == other.generated_nodes
        )

    def __hash__(self):
        return hash(self.final_state)


class LocalSolution(Solution):
    def __init__(self, algorithm: SearchAlgorithm, problem: Problem, heuristic: Callable[[Node], float], params: list):
        super().__init__(algorithm, problem, heuristic, params)
        self.depth = node.depth
        self.iterations = node.visited_nodes
        self.initial = problem.initial_state
        self.better_state = node.state
        self.generated_nodes = node.generated_nodes

    pass




class NullSolution(Solution):
    def __init__(
        self,
        algorithm: SearchAlgorithm,
        problem: Problem,
        heuristic: Callable[[Node], float],
        run_time: float,
        params: list,
    ):
        super().__init__(algorithm, problem, heuristic, params=params)
        self.path = "-"
        self.path_cost = "-"
        self.action_sequence = "-"
        self.depth = "-"
        self.run_time = run_time
        self.occupied_memory = "-"
        self.generated_nodes = "-"
        self.memory = "-"
        self.approx_memory_generated = "-"
        self.average_branching_factor = "-"
        self.max_nodes_in_frontier = "-"
        self.visited_ones = "-"
        self.no_leaf_nodes = "-"
        self.final_state = "Time Exceeded"

    def __eq__(self, other):
        return (
            super().__eq__(other)
            and self.final_state == other.final_state
            and self.path == other.path
            and self.path_cost == other.path_cost
            and self.action_sequence == other.action_sequence
            and self.depth == other.depth
            and self.run_time == other.run_time
            and self.memory == other.memory
            and self.generated_nodes == other.generated_nodes
        )

    def __hash__(self):
        return hash(self.final_state)
