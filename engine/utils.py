class Utils:
    """
    def compare_searchers(self, problems, header):
        bfs_graph = BreadthFirstVisitedSearch()
        dfs = DepthFirstSearch()
        dfs_graph = DepthFirstVisitedSearch()
        searchers = [bfs_graph, dfs, dfs_graph]

        last_nodes = [s.search(problems[0]) for s in searchers]
        solutions = [n.solution() for n in last_nodes]

        # Create table - Name of searcher | Path | Solution State
        table = []
        for i in range(len(searchers)):
            table.append(
                [searchers[i].__class__.__name__, [name(p) for p in solutions[i]], last_nodes[i].state.get_state()])

        print("\n")
        print_table(table, header)
    """

    def inversion_count(self, state: tuple) -> int:
        inversion_counter = 0
        for i in range(len(state) - 1):
            for j in range(i + 1, len(state)):
                if state[i] > state[j] and state[i] != 0 and state[j] != 0:
                    inversion_counter = inversion_counter + 1
        return inversion_counter


utils = Utils()
