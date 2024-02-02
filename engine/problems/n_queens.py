from engine.problems.problem import Problem, State, Action
from constants import NQUEENS
from framework.factories.n_queens_config_generator import NQueensStateFactory

class NQueenState(State):
    def __init__(self, board):
        super().__init__(board)
        self.N = len(board)
        if not self.is_valid():
            print(self.data)
            raise ValueError("Invalid board")

    def is_goal(self) -> bool:
        for col in range(self.N):
            if self.data[col] == -1 or self.conflicted(self.data[col], col):
                return False
        return True

    def is_valid(self) -> bool:
        for col in self.data:
            if col < 0 or col > self.N - 1:
                return False
        return True

    def conflicted(self, row1: int, col1: int) -> bool:
        for col2 in range(col1 + 1, self.N):
            row2 = self.data[col2]
            if self.check_conflict(row1, col1, row2, col2):
                return True
        return False

    def check_conflict(self, row1: int, col1: int, row2: int, col2: int) -> bool:
        return (
            row1 == row2
            or row1 - col1 == row2 - col2  # same row
            or row1 + col1 == row2 + col2  # same \ diagonal
        )  # same / diagonal

    def __eq__(self, other) -> bool:
        return isinstance(other, NQueenState) and self.data == other.data

    def __hash__(self) -> int:
        tup = tuple(self.data)
        return hash(tup)


class NQueensActions(Action):
    def is_enabled(self, state: NQueenState, col: int) -> bool:
        raise NotImplementedError

    def execute(self, state: NQueenState) -> NQueenState:
        raise NotImplementedError


class NQueensProblem(Problem):
    def __init__(self, initial: NQueenState):
        super().__init__([Up(), Down()], initial)

    def actions(self, state: NQueenState) -> list[Action]:
        result = []
        for col in range(self.initial.N):
            for action in self.problem_actions:
                if action.is_enabled(state, col):
                    result.append(NQueenActionDecorator(col, action))
        return result

    def __repr__(self):
        return NQUEENS
    
class NQueenActionBruteMoves():
    def __init__(self, col, row):
        self.col = col
        self.row = row
    
    def is_enabled(self, state: NQueenState) -> bool:
        return state.data[self.col] != self.row
    
    def execute(self, state: NQueenState) -> NQueenState:
        new_data = [(self.row if col == self.col else q) for col, q in enumerate(state.data)]
        return NQueenState(new_data)


class NQueensProblemBrute(Problem):
    def __init__(self, initial: NQueenState):
        super().__init__([], initial)

    def actions(self, state: NQueenState) -> list[Action]:
        actions = [NQueenActionBruteMoves(col, row) for col in range(self.initial.N) for row in range(self.initial.N) if state.data[col] != row]
        return actions

    def factory(self) -> NQueensStateFactory:
        return NQueensStateFactory(self.initial.N)

    def __repr__(self):
        return NQUEENS


class NQueenActionDecorator:
    def __repr__(self):
        if isinstance(self.action, Up):
            return "Up"
        return "Down"

    def __init__(self, col, action):
        self.col = col
        self.action = action

    def execute(self, state):
        return self.action.execute(state, self.col)

    def inverse(self):
        return self.action.inverse()

    def __eq__(self, other):
        return (
            self.action == other.action
            if isinstance(other, NQueenActionDecorator)
            else self.action == other
        )


class Up(NQueensActions):
    def __repr__(self):
        return "Up"

    def is_enabled(self, state: NQueenState, col: int) -> bool:
        return state.data[col] >= 1

    def execute(self, state: NQueenState, col: int) -> NQueenState:
        new_data = state.data.copy()
        new_data[col] -= 1
        return NQueenState(new_data)

    def inverse(self):
        return Down()

    def __eq__(self, other):
        return (
            isinstance(other, Up)
            or isinstance(other, NQueenActionDecorator)
            and isinstance(other.action, Up)
        )


class Down(NQueensActions):
    def __repr__(self):
        return "Down"

    def is_enabled(self, state: NQueenState, col: int) -> bool:
        return state.data[col] < state.N - 1

    def execute(self, state: NQueenState, col: int) -> NQueenState:
        new_state = state.data.copy()
        new_state[col] += 1
        return NQueenState(new_state)

    def inverse(self):
        return Up()

    def __eq__(self, other):
        return (
            isinstance(other, Down)
            or isinstance(other, NQueenActionDecorator)
            and isinstance(other.action, Down)
        )
