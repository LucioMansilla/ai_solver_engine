from engine.algorithms.informed.greedy_best_first_search import GreedyBestFirstSearch


class UniformCostSearch(GreedyBestFirstSearch):
    def __init__(self):
        super().__init__(lambda node: node.path_cost)
