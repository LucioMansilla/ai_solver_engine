from engine.heuristics.dummy import dummy
from engine.heuristics.romania_heuristics import euclidean_distance


class RomaniaHeuristicFactory:
    heuristics = {"EuclideanDistance": euclidean_distance, "NonHeuristic": dummy}

    @staticmethod
    def create(heuristic_name: str) -> callable:
        if heuristic_name in RomaniaHeuristicFactory.heuristics:
            return RomaniaHeuristicFactory.heuristics[heuristic_name]
        else:
            raise ValueError("Non valid heuristic.")

    @classmethod
    def heuristic_names(cls) -> list[str]:
        return ["EuclideanDistance"]
