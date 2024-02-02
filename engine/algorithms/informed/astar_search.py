from engine.algorithms.informed.greedy_best_first_search import GreedyBestFirstSearch


class AStarSearch(GreedyBestFirstSearch):
    def __init__(self, heuristic):
        super().__init__(lambda node: heuristic(node) + node.path_cost)
