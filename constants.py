from engine.data_structures.graph import UndirectedGraph
from engine.algorithms.informed.astar_search import AStarSearch
from engine.algorithms.informed.greedy_best_first_search import GreedyBestFirstSearch
from engine.algorithms.uninformed.breadth_first_search import (
    BreadthFirstSearch,
    BreadthFirstVisitedSearch,
    BreadthFirstAcyclicSearch,
)
from engine.algorithms.uninformed.depth_first_search import (
    DepthFirstSearch,
    DepthFirstAcyclicSearch,
    DepthFirstVisitedSearch,
)
from engine.algorithms.uninformed.iterative_deepening import IterativeDeepening
from engine.algorithms.uninformed.uniform_cost_search import UniformCostSearch
from engine.algorithms.uninformed.bidirectional_search import BidirectionalSearch
from engine.algorithms.local.hill_climbing import HillClimbingSearch, HillClimbingSearchWithRandomRestarts, HillClimbingSearchWithSidewaysMoves

from engine.factories.heuristic_factories.n_puzzle_heuristic_factory import (
    NPuzzleHeuristicFactory,
)
from engine.factories.heuristic_factories.n_queens_heuristic_factory import (
    NQueensHeuristicFactory,
)
from engine.factories.heuristic_factories.romania_heuristic_factory import (
    RomaniaHeuristicFactory,
)


CUT_OFF = "cut_off"

OUTPUTS_PATH = "framework/storage/outputs/"
GENERATED_STATES_PATH = "framework/storage/generated_states/"

ROMANIA_MAP = UndirectedGraph.undirected_graph(
    dict(
        Arad=dict(Zerind=75, Sibiu=140, Timisoara=118),
        Bucharest=dict(Urziceni=85, Pitesti=101, Giurgiu=90, Fagaras=211),
        Craiova=dict(Drobeta=120, Rimnicu=146, Pitesti=138),
        Drobeta=dict(Mehadia=75),
        Eforie=dict(Hirsova=86),
        Fagaras=dict(Sibiu=99),
        Hirsova=dict(Urziceni=98),
        Iasi=dict(Vaslui=92, Neamt=87),
        Lugoj=dict(Timisoara=111, Mehadia=70),
        Oradea=dict(Zerind=71, Sibiu=151),
        Pitesti=dict(Rimnicu=97),
        Rimnicu=dict(Sibiu=80),
        Urziceni=dict(Vaslui=142),
    )
)

ROMANIA_DISTANCES = dict(
    Arad=(91, 492),
    Bucharest=(400, 327),
    Craiova=(253, 288),
    Drobeta=(165, 299),
    Eforie=(562, 293),
    Fagaras=(305, 449),
    Giurgiu=(375, 270),
    Hirsova=(534, 350),
    Iasi=(473, 506),
    Lugoj=(165, 379),
    Mehadia=(168, 339),
    Neamt=(406, 537),
    Oradea=(131, 571),
    Pitesti=(320, 368),
    Rimnicu=(233, 410),
    Sibiu=(207, 457),
    Timisoara=(94, 410),
    Urziceni=(456, 350),
    Vaslui=(509, 444),
    Zerind=(108, 531),
)

##----------------- GLOBAL CONSTANTS -----------------##

NPUZZLE = "NPuzzle"
NQUEENS = "NQueens"
ROMANIA = "Romania"

AVAILABLE_PROBLEMS = [NPUZZLE, NQUEENS, ROMANIA]
INFORMED_ALGORITHMS = {
    "GreedyBestFirstSearch": GreedyBestFirstSearch,
    "A*": AStarSearch,
}
UNINFORMED_ALGORITHMS = {
    "BreadthFirstSearch": BreadthFirstSearch,
    "BreadthFirstVisitedSearch": BreadthFirstVisitedSearch,
    "BreadthFirstAcyclicSearch": BreadthFirstAcyclicSearch,
    "DepthFirstSearch": DepthFirstSearch,
    "DepthFirstAcyclicSearch": DepthFirstAcyclicSearch,
    "DepthFirstVisitedSearch": DepthFirstVisitedSearch,
    "UniformCostSearch": UniformCostSearch,
    "IterativeDeepening": IterativeDeepening,
    "BidirectionalSearch": BidirectionalSearch,
}

LOCAL_ALGORITHMS = {
    "HillClimbingSearch":HillClimbingSearch,
    "HillClimbingSearchWithSidewaysMoves": HillClimbingSearchWithSidewaysMoves,
    "HillClimbingSearchWithRandomRestarts": HillClimbingSearchWithRandomRestarts
}

HEURISTIC_FACTORIES = {
    NPUZZLE: NPuzzleHeuristicFactory,
    NQUEENS: NQueensHeuristicFactory,
    ROMANIA: RomaniaHeuristicFactory,
}

## GENERATOR CONSTANTS ##
BETTER_ALGORITHM = "A*"
BETTER_HEURISTIC = {
    NPUZZLE: "Manhattan",
    NQUEENS: "CountConflictedQueens",
    ROMANIA: "EuclideanDistance",
}

MULTIPLIER = {"mix": 2, "hard": 1}

DUMMY = "dummy"
