import time
import tracemalloc

from engine.core.solution import Solution
from engine.factories.solution_factory import SolutionFactory
from engine.factories.algorithm_factory import AlgorithmFactory
from engine.factories.problem_factory import ProblemFactory


class Engine:
    def __init__(self, problem: str, algorithm: str, heuristic: str = "NonHeuristic"):
        self.heuristic_name = heuristic
        self.params = problem[1:]
        self.problem, HeuristicFactory = ProblemFactory.create(problem)
        self.heuristic = HeuristicFactory.create(heuristic)
        self.algorithm = AlgorithmFactory.create(algorithm, self.heuristic)

    def solve(self) -> Solution:
        start_time, current = self.initialize_trace()
        self.print_info()
        node_solution = self.algorithm.search(self.problem)
        memory,run_time = self.stop_trace(start_time,current)
        return SolutionFactory.create(node_solution, self.algorithm, self.problem, self.heuristic, run_time, memory, self.params)

    def print_info(self):
        print("Algorithm: ", self.algorithm.__class__.__name__)
        print("Problem: ", self.problem)
        if self.heuristic_name != "NonHeuristic":
            print("Heuristic: ", self.heuristic.__name__.capitalize())
        else:
            print("Heuristic: --")
        
        print("Solving....")
        
    def initialize_trace(self):
        start_time = time.time()
        tracemalloc.start()
        current, peak = tracemalloc.get_traced_memory()
        return start_time, current

    def stop_trace(self, start_time, current):
        tracemalloc.stop()
        end_time = time.time()
        end_current, peak = tracemalloc.get_traced_memory()
        memory = current - end_current
        run_time = end_time - start_time
        print("Finished in: ", round(run_time, 4), " seconds")
        return memory, run_time