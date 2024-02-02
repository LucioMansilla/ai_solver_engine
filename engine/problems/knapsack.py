from engine.problems.problem import Problem, Action, State


class KnapsackState(State):
    def __init__(self, state: list, weights: list, capacity: int, values: list):
        super().__init__(state)
        self.weights = weights
        self.capacity = capacity
        self.values = values

    def is_goal(self) -> bool:
        return False

    @property
    def sack_value(self) -> int:
        return sum([self.values[i] for i in range(len(self.data)) if self.data[i] == 1])

    @property
    def sack_weight(self) -> int:
        return sum(
            [self.weights[i] for i in range(len(self.data)) if self.data[i] == 1]
        )



class PutInKnapSack(Action):
    def __init__(self, item: int):
        self.item = item

    def __repr__(self):
        return f"Put {self.item} in knapsack"

    def is_enabled(self, state: KnapsackState) -> bool:
        return state.data[self.item] == 0

    def execute(self, state: KnapsackState) -> KnapsackState:
        new_state = state.data.copy()
        new_state[self.item] = 1
        return KnapsackState(new_state, state.weights, state.capacity, state.values)

    # def inverse(self):
    #  11 -> 01 -> 00 -> 10 -> 11
    #   return Remove
    # FromKnapSack(self.item)

    def __eq__(self, other) -> bool:
        return isinstance(other, PutInKnapSack) and self.item == other.item


class KnapSackProblem(Problem):
    def __init__(self, initial: KnapsackState):
        super().__init__([PutInKnapSack(i) for i in range(len(initial.data))], initial)

    def __repr__(self):
        return "Knapsack"
