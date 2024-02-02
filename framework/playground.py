from engine.core.engine import Engine

def prueba_chiteada():
    state = (2, 3, 0, 7, 4, 6, 5, 1, 8)
    e = Engine(["NPuzzle", state], "A*", "Gaschnig")

    # print("Empezando en el state: ", state)
    solution = e.solve()
    # report_to_csv([solution], 'testear.csv')
    print(solution)


# [0,2,4,6,1,3,5,7]


def prueba_n_queens():
    # final_State [2,0,3,1]
    e = Engine(["NQueens", [4, 4, 3, 2, 1, 5, 6, 7]], "A*", "CountConflictedQueens")
    solution = e.solve()
    print(solution)


def prueba_romania():
    state = ("Drobeta", "Sibiu")
    e = Engine(["Romania", state], "BidirectionalSearch")
    solution = e.solve()
    print(solution)


def romania_prueba_inverted():
    e = Engine(["Romania", "Arad", "Bucharest"], "BidirectionalSearch")
    solution = e.solve()
    print(solution)


def prueba_bidirectional():
    state = (1, 8, 2, 0, 4, 3, 7, 6, 5)
    e = Engine(["NPuzzle", state], "A*", "EuclideanDistance")
    solution = e.solve()
    print(solution)


def prueba_chiteada2():
    from framework.filemanager.solution_file_manager import SolutionFileManager

    state = ("Arad", "Bucharest")
    e = Engine(["Romania", state], "A*", "EuclideanDistance")
    solution = e.solve()
    SolutionFileManager.write_to_csv([solution], "testear.csv")
    print(solution)


def prueba_algorithms():
    uninformed = UNINFORMED_ALGORITHMS = [
        "BreadthFirstSearch",
        "BreadthFirstVisitedSearch",
        "BreadthFirstAcyclicSearch",
        "DepthFirstAcyclicSearch",
        "UniformCostSearch",
        "IterativeDeepening",
    ]
    states = (1, 2, 0, 5, 6, 3, 4, 7, 8)
    print("Prueba Romania")
    for algorithm in uninformed:
        e = Engine(["NPuzzle", states], algorithm)
        solution = e.solve()
        print(solution)
    """    
        utils_test/estado_problem/: if dict[problem](estado).is_goal()
    dict ={
        'NPuzzle': NPuzzleState,
        'NQueens': NQueensState,
        'Romania': RomaniaState
    }
    """


def prueba_knapsack(): # 80
    state = [0, 0, 0, 0]
    weights = [2, 5, 10, 5]
    values = [20, 30, 50, 10]
    capacity = 16
    from engine.algorithms.local.hill_climbing import HillClimbingSearch
    from engine.heuristics.knapsack import sum_weighted
    from engine.problems.knapsack import KnapsackState, KnapSackProblem

    algorithm = HillClimbingSearch(sum_weighted)
    problem = KnapSackProblem((KnapsackState(state, weights, capacity, values)))
    sol = algorithm.search(problem)
    print(sol.state.sack_value)
    print("Weights: ", sol.state.sack_weight)


def prueba_knapsack_2(): # 3
    """
    Input:
    N = 3
    W = 4
    values[] = {1,2,3}
    weight[] = {4,5,1}
    Output: 3
    """
    state = [0, 0, 0]
    weights = [4, 5, 1]
    values = [1, 2, 3]
    capacity = 4
    from engine.algorithms.local.hill_climbing import HillClimbingSearch
    from engine.heuristics.knapsack import sum_weighted
    from engine.problems.knapsack import KnapsackState, KnapSackProblem

    algorithm = HillClimbingSearch(sum_weighted)
    problem = KnapSackProblem((KnapsackState(state, weights, capacity, values)))
    sol = algorithm.search(problem)
    print(sol.state.sack_value)
    print("Weights: ", sol.state.sack_weight)

    
def prueba_kanpsack_3(): #220
    state = [0, 0, 0]
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50
    from engine.algorithms.local.hill_climbing import HillClimbingSearch
    from engine.heuristics.knapsack import sum_weighted
    from engine.problems.knapsack import KnapsackState, KnapSackProblem
    algorithm = HillClimbingSearch(sum_weighted)
    problem = KnapSackProblem((KnapsackState(state, weights, capacity, values)))
    sol = algorithm.search(problem)
    print(sol.state.sack_value)
    print("Weights: ", sol.state.sack_weight)

def prueba_n_queens_climbing():
    from framework.factories.n_queens_config_generator import NQueensConfigGenerator
    from engine.algorithms.local.hill_climbing import HillClimbingSearch,HillClimbingSearchWithSidewaysMoves
    from engine.heuristics.knapsack import sum_weighted
    from engine.problems.knapsack import KnapsackState, KnapSackProblem
    from engine.heuristics.n_queens_heuristics import inverse_count_conflicted_queens
    from engine.problems.n_queens import NQueenState, NQueensProblem,NQueensProblemBrute


    queens_states = NQueensConfigGenerator

    hill_climbing_config = NQueensConfigGenerator.create(8, 100)
    count_goals = 0
    for current_state in hill_climbing_config:
        problem = NQueensProblemBrute(NQueenState(current_state))
        algorithm = HillClimbingSearch(inverse_count_conflicted_queens)
        solution = algorithm.search(problem)
        if solution.state.is_goal():
            count_goals += 1
    print(count_goals)

def prueba_n_queens_restarts_climbing():
    from framework.factories.n_queens_config_generator import NQueensConfigGenerator
    from engine.algorithms.local.hill_climbing import HillClimbingSearchWithRandomRestarts
    from engine.heuristics.knapsack import sum_weighted
    from engine.problems.knapsack import KnapsackState, KnapSackProblem
    from engine.heuristics.n_queens_heuristics import count_conflicted_queens
    from engine.problems.n_queens import NQueenState, NQueensProblem,NQueensProblemBrute


    queens_states = NQueensConfigGenerator

    hill_climbing_config = NQueensConfigGenerator.create(8, 100)
    count_goals = 0
    for current_state in hill_climbing_config:
        problem = NQueensProblemBrute(NQueenState(current_state))
        algorithm = HillClimbingSearchWithRandomRestarts(count_conflicted_queens)
        solution = algorithm.search(problem)
        if solution and solution.state.is_goal():
            print(solution.state.data)
            count_goals += 1
    print(count_goals)


def prueba_nqueens_del_test():
    e = Engine(["NQueens", [4, 4, 3, 2, 1, 5, 6, 7]], 'GreedyBestFirstSearch', "CountConflictedQueens")
    solution = e.solve()
    print(solution)

if __name__ == "__main__":
    prueba_nqueens_del_test()

