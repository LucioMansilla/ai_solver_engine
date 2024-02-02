from engine.heuristics.dummy import dummy
from engine.heuristics.n_queens_heuristics import count_conflicted_queens


class NQueensHeuristicFactory:
    heuristics = {
        "CountConflictedQueens": count_conflicted_queens,
        "NonHeuristic": dummy,
    }

    @staticmethod
    def create(heuristic_name: str) -> callable:
        if heuristic_name in NQueensHeuristicFactory.heuristics:
            return NQueensHeuristicFactory.heuristics[heuristic_name]
        else:
            raise ValueError("Non valid heuristic.")

    @classmethod
    def heuristic_names(cls) -> list[str]:
        return ["CountConflictedQueens"]
