from constants import LOCAL_ALGORITHMS
from engine.core.solution import LocalSolution, StatisticalSolution, NonSolution, Solution


class SolutionFactory:
    
    @classmethod
    def create(cls, node_solution, algorithm, problem, heuristic, run_time, memory, params) -> Solution:
        if node_solution and algorithm in LOCAL_ALGORITHMS:
            return LocalSolution(
                algorithm=algorithm,
                problem=problem,
                heuristic=heuristic,
                params=params
            )
        elif node_solution:
            return StatisticalSolution(
                node=node_solution,
                algorithm=algorithm,
                problem=problem,
                heuristic=heuristic,
                run_time=run_time,
                memory=memory,
                params=params
            )
        else:
            return NonSolution(
                node=node_solution,
                algorithm=algorithm,
                problem=problem,
                heuristic=heuristic,
                run_time=run_time,
                memory=memory,
                params=params
            )