from engine.heuristics.dummy import dummy
from constants import INFORMED_ALGORITHMS, UNINFORMED_ALGORITHMS
from engine.algorithms.search_algorithm import SearchAlgorithm


class AlgorithmFactory:
    @classmethod
    def create(cls, algorithm: str, h: callable) -> SearchAlgorithm:
        if algorithm in UNINFORMED_ALGORITHMS and h == dummy:
            return UNINFORMED_ALGORITHMS[algorithm]()
        elif algorithm in INFORMED_ALGORITHMS and h != dummy:
            return INFORMED_ALGORITHMS[algorithm](h)
        else:
            raise Exception("Algorithm Not Found")
