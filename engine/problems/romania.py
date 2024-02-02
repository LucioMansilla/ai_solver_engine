from constants import ROMANIA_MAP, ROMANIA
from engine.problems.problem import Problem, Action, State


class RomaniaState(State):
    def __init__(self, state: tuple):
        super().__init__(state)
        self.current_city = state[0]
        self.goal_city = state[1]

    def is_goal(self) -> bool:
        return self.current_city == self.goal_city

    def is_valid(self) -> bool:
        nodes = list(ROMANIA_MAP.nodes())
        return self.current_city in nodes and self.goal_city in nodes

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, RomaniaState) and self.current_city == other.current_city
        )

    def __hash__(self) -> int:
        return hash(self.current_city)

    def __repr__(self):
        return f"{self.current_city}"


class RomaniaAction(Action):
    def __init__(self, origin: str, destination: str, cost: float):
        self.origin = origin
        self.destination = destination
        self.cost = cost

    def __repr__(self):
        return f"({self.origin} -> {self.destination}, {self.cost})"

    def is_enabled(self, state: RomaniaState) -> bool:
        return state.current_city == self.origin

    def execute(self, state: RomaniaState) -> RomaniaState:
        new_tuple = (self.destination, state.goal_city)
        return RomaniaState(new_tuple)

    def inverse(self):
        return RomaniaAction(self.destination, self.origin, self.cost)

    def __eq__(self, other) -> bool:
        return isinstance(other, RomaniaAction) and self.__repr__() == other.__repr__()


class RomaniaProblem(Problem):
    def __repr__(self) -> str:
        return ROMANIA

    def __init__(self, initial: RomaniaState):
        super().__init__([], initial)
        self.graph = ROMANIA_MAP

    def actions(self, state: RomaniaState) -> list[RomaniaAction]:
        neighbors_dict = self.graph.get(state.current_city)
        return [
            RomaniaAction(state.current_city, neighbor, cost)
            for neighbor, cost in neighbors_dict.items()
        ]

    def path_cost(
        self, cost_so_far: float, a: str, action: RomaniaAction, b: str
    ) -> float:
        return cost_so_far + action.cost

    def inverse(self) -> Problem:
        inverted_initial = RomaniaState(
            (self.initial.goal_city, self.initial.current_city)
        )
        return RomaniaProblem(inverted_initial)
