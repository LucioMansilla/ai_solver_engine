from engine.heuristics.dummy import dummy
from engine.heuristics.n_puzzle_heuristics import (
    incorrect_placed_squares,
    manhattan,
    gaschnig,
    euclidean_distance,
)


class NPuzzleHeuristicFactory:
    heuristics = {
        "IncorrectPlacedSquares": incorrect_placed_squares,
        "Manhattan": manhattan,
        "Gaschnig": gaschnig,
        "EuclideanDistance": euclidean_distance,
        "NonHeuristic": dummy,
    }

    @staticmethod
    def create(heuristic_name: str) -> callable:
        if heuristic_name in NPuzzleHeuristicFactory.heuristics:
            return NPuzzleHeuristicFactory.heuristics[heuristic_name]
        else:
            raise ValueError("Non valid heuristic.")

    @classmethod
    def heuristic_names(cls) -> list[str]:
        return ["IncorrectPlacedSquares", "Manhattan", "Gaschnig", "EuclideanDistance"]
