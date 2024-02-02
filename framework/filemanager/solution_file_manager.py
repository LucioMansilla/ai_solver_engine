from constants import NPUZZLE, NQUEENS
import csv


class SolutionFileManager:
    headers = [
        "Problem Name",
        "Params",
        "Algorithm",
        "Heuristic",
        "Initial State",
        "Final State",
        "Path",
        "Path Cost",
        "Action Sequence",
        "Run Time",
        "Memory Used",
        "Depth",
        "Branching Factor",
        "Generated Nodes",
        "Visited Nodes",
        "Max Nodes in Frontier",
        "No Leaf Nodes",
        "Brute Memory Generated",
    ]

    @classmethod
    def create_params(cls, problem_name: str, state: tuple) -> str:
        if str(problem_name) == NPUZZLE:
            return state.get_puzzle_number()
        elif str(problem_name) == NQUEENS:
            return len(state.data)
        return state.current_city + "->" + state.goal_city

    @classmethod
    def write_to_csv(cls, solutions: list, file_name: str):
        for solution in solutions:
            if file_name[len(file_name) - 4 :] != ".csv":
                file_name = file_name + ".csv"
            with open(f"{file_name}", "a", encoding="UTF8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=cls.headers)
                if f.tell() == 0:
                    writer.writeheader()
                writer.writerow(
                    {
                        "Problem Name": solution.problem_name,
                        "Params": cls.create_params(
                            solution.problem_name, solution.problem_name.initial
                        ),
                        "Algorithm": solution.algorithm,
                        "Heuristic": solution.heuristic,
                        "Initial State": solution.initial_state,
                        "Final State": solution.final_state,
                        "Path": solution.path,
                        "Path Cost": str(solution.path_cost),
                        "Action Sequence": solution.action_sequence,
                        "Run Time": str(solution.run_time),
                        "Memory Used": solution.memory,
                        "Depth": str(solution.depth),
                        "Branching Factor": str(solution.average_branching_factor),
                        "Generated Nodes": str(solution.generated_nodes),
                        "Visited Nodes": str(solution.visited_ones),
                        "Max Nodes in Frontier": str(solution.max_nodes_in_frontier),
                        "No Leaf Nodes": str(solution.no_leaf_nodes),
                        "Brute Memory Generated": solution.approx_memory_generated,
                    }
                )
