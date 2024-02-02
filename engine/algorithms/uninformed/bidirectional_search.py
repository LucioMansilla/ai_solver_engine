from collections import deque
from engine.data_structures.node import Node
from engine.algorithms.search_algorithm import SearchAlgorithm
from engine.problems.problem import Problem, State, Action


class BidirectionalSearch(SearchAlgorithm):
    def search(self, problem_f: Problem) -> Node | None:
        problem_b = problem_f.inverse()
        initial_state_f = problem_f.initial_state()
        initial_state_b = problem_b.initial_state()
        frontier_f = deque([Node(initial_state_f)])
        frontier_b = deque([Node(initial_state_b)])
        reached_f = {}
        reached_b = {}
        solution = None
        is_f_turn = True
        while not solution and frontier_f and frontier_b:
            if is_f_turn:
                solution = self.proceed(
                    is_f_turn, problem_f, frontier_f, reached_f, reached_b, solution
                )
            else:
                solution = self.proceed(
                    is_f_turn, problem_b, frontier_b, reached_b, reached_f, solution
                )
            is_f_turn = not is_f_turn

        problem_f.generated_nodes += problem_b.generated_nodes
        problem_f.visited_ones += problem_b.visited_ones

        return solution

    def proceed(
        self,
        is_f_turn: bool,
        problem: Problem,
        frontier: deque[Node],
        reached: dict,
        reached2: dict,
        solution: Node,
    ) -> Node | None:
        node = frontier.popleft()

        problem.visited_ones += 1

        for child in node.expand(problem):
            s = child.state
            if s not in reached:
                reached[s] = child
                frontier.append(child)
                if s in reached2:
                    solution = self.join_nodes(is_f_turn, child, reached2[s])
        return solution

    def join_nodes(
        self, is_f_turn: bool, first_node: Node, second_node: Node
    ) -> Node | None:
        if not is_f_turn:
            first_node, second_node = second_node, first_node

        second_path = self.get_reverse_path(second_node)

        current_node = first_node
        back_action = second_node.action.inverse()
        for backwards_node in second_path:
            cost = back_action.cost
            current_node = self.create_new_node(
                current_node, backwards_node.state, cost, back_action
            )
            back_action = (
                backwards_node.action.inverse() if backwards_node.action else None
            )

        return current_node

    def get_reverse_path(self, node: Node) -> list[Node]:
        return node.path()[::-1][1:] if node else []

    def create_new_node(
        self, parent: Node, state: State, cost: float, action: Action
    ) -> Node:
        return Node(
            parent=parent, state=state, path_cost=parent.path_cost + cost, action=action
        )
