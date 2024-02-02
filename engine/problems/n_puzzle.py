from math import sqrt

from engine.problems.problem import Problem, State, Action
from engine.utils import utils
from constants import NPUZZLE
from framework.factories.n_puzzle_config_generator import NPuzzleConfigGenerator
class NPuzzleState(State):
    def __init__(self, state: tuple, n: int = None, index_of_blank_square: int = None):
        super().__init__(state)
        if n is None:
            self.n = len(state)
            self.index_blank_square = state.index(0)
        else:
            self.n = n + 1
            self.index_blank_square = index_of_blank_square

        self.sqrt_n = int(sqrt(self.n + 1))

    def get_puzzle_number(self) -> int:
        return self.n - 1

    def get_state(self) -> tuple:
        return self.data

    def get_index_blank_square(self) -> int:
        return self.index_blank_square

    def is_goal(self) -> bool:
        list_n1 = list(self.data[:-1])
        return list_n1 == sorted(list_n1) and self.data[-1] == 0

    def is_blank_square_on_left_edge(self) -> bool:
        return self.index_blank_square % self.sqrt_n == 0

    def is_blank_square_on_right_edge(self) -> bool:
        return self.index_blank_square % self.sqrt_n == self.sqrt_n - 1

    def is_blank_square_on_top_edge(self) -> bool:
        return self.index_blank_square < self.sqrt_n

    def is_blank_square_on_bottom_edge(self) -> bool:
        return self.index_blank_square >= self.n - self.sqrt_n

    def is_valid(self) -> bool:
        if not float.is_integer(sqrt(self.n)):
            return False

        number_inv = utils.inversion_count(self.data)
        if self.n % 2 == 1:
            return number_inv % 2 == 0
        else:
            if self.__is_blank_square_on_even_row_from_bottom():
                return number_inv % 2 == 1
            else:
                return number_inv % 2 == 0

    def __is_blank_square_on_even_row_from_bottom(self) -> bool:
        return (self.sqrt_n - self.__get_row_of_blank_square()) % 2 == 0

    def __get_row_of_blank_square(self) -> int:
        return self.index_blank_square // self.sqrt_n

    def __eq__(self, other) -> bool:
        return isinstance(other, NPuzzleState) and self.data == other.data

    def __hash__(self) -> int:
        return hash(self.data)


class InvertedNPuzzleProblem(Problem):
    def __init__(self, initial: NPuzzleState, goal=None):
        self.goal = goal
        super().__init__([Up(), Down(), Left(), Right()], initial)

    def goal_test(self, state: State) -> bool:
        return state == self.goal


class NPuzzleProblem(Problem):
    def __init__(self, initial: NPuzzleState):
        super().__init__([Up(), Down(), Left(), Right()], initial)

    def __repr__(self):
        return NPUZZLE

    def inverse(self) -> InvertedNPuzzleProblem:
        goal_list = [i for i in range(1, self.initial.n)]
        goal_list.append(0)
        goal_state = NPuzzleState(tuple(goal_list))
        return InvertedNPuzzleProblem(initial=goal_state, goal=self.initial)
    
    def factory(self):
        return NPuzzleConfigGenerator(self.initial.n)
    
    #problem_factory = problem.factory()
    #new_state = problem_factory.create_state()


class NPuzzleAction(Action):
    def swap(self, arr: list, idx1: int, idx2: int) -> list:
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
        return arr

    def move_blank_square(
        self, state: NPuzzleState, actual_pos: int, next_pos: int
    ) -> tuple:
        return tuple(self.swap(list(state.get_state()), actual_pos, next_pos))

    def is_enabled(self, state: NPuzzleState) -> bool:
        raise NotImplementedError

    def execute(self, state: NPuzzleState) -> NPuzzleState:
        raise NotImplementedError

    def inverse(self) -> Action:
        raise NotImplementedError

    def __eq__(self, other) -> bool:
        return isinstance(other, NPuzzleAction) and self.__repr__() == other.__repr__()


class Up(NPuzzleAction):
    def __repr__(self):
        return "Up"

    def is_enabled(self, state: NPuzzleState) -> bool:
        return not state.is_blank_square_on_top_edge()

    def execute(self, state: NPuzzleState) -> NPuzzleState:
        actual_pos = state.get_index_blank_square()
        next_pos = actual_pos - state.sqrt_n
        next_state = self.move_blank_square(state, actual_pos, next_pos)
        return NPuzzleState(next_state, state.get_puzzle_number(), next_pos)

    def inverse(self) -> NPuzzleAction:
        return Down()


class Down(NPuzzleAction):
    def __repr__(self):
        return "Down"

    def is_enabled(self, state: NPuzzleState) -> bool:
        return not state.is_blank_square_on_bottom_edge()

    def execute(self, state: NPuzzleState) -> NPuzzleState:
        actual_pos = state.get_index_blank_square()
        next_pos = actual_pos + state.sqrt_n
        next_state = self.move_blank_square(state, actual_pos, next_pos)
        return NPuzzleState(next_state, state.get_puzzle_number(), next_pos)

    def inverse(self) -> NPuzzleAction:
        return Up()


class Left(NPuzzleAction):
    def __repr__(self):
        return "Left"

    def is_enabled(self, state: NPuzzleState) -> bool:
        return not state.is_blank_square_on_left_edge()

    def execute(self, state: NPuzzleState) -> NPuzzleState:
        actual_pos = state.get_index_blank_square()
        next_pos = actual_pos - 1
        next_state = self.move_blank_square(state, actual_pos, next_pos)
        return NPuzzleState(next_state, state.get_puzzle_number(), next_pos)

    def inverse(self) -> NPuzzleAction:
        return Right()


class Right(NPuzzleAction):
    def __repr__(self):
        return "Right"

    def is_enabled(self, state: NPuzzleState) -> bool:
        return not state.is_blank_square_on_right_edge()

    def execute(self, state: NPuzzleState) -> NPuzzleState:
        actual_pos = state.get_index_blank_square()
        next_pos = actual_pos + 1
        next_state = self.move_blank_square(state, actual_pos, next_pos)
        return NPuzzleState(next_state, state.get_puzzle_number(), next_pos)

    def inverse(self) -> NPuzzleAction:
        return Left()
