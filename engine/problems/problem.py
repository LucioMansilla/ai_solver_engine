class State:
    def __init__(self, data):
        self.data = data

    def is_goal(self) -> bool:
        """Method that returns a boolean depending if the state is a final state"""
        raise NotImplementedError

    def is_valid(self) -> bool:
        """Method repOK that returns a boolean depending if the state is a valid state."""
        raise NotImplementedError


class Action:
    """ " Return true if the action is enabled in the given state"""

    def __init__(self) -> None:
        self.cost = 1

    def is_enabled(self, state: State) -> bool:
        raise NotImplementedError

    """" Execute the action in the given state"""

    def execute(self, state: State) -> State:
        raise NotImplementedError


class Problem:
    """The abstract class for a formal problem. You should subclass
    this and implement the methods actions and result, and possibly
    __init__, goal_test, and path_cost. Then you will create instances
    of your subclass and solve them with the various search functions."""

    def __init__(self, actions: list[Action], initial: State):
        """The constructor"""
        self.initial = initial
        self.problem_actions = actions

    """Return the initial state for the problem."""

    def initial_state(self) -> State:
        return self.initial

    def actions(self, state: State) -> list[Action]:
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""
        result = []
        for action in self.problem_actions:
            if action.is_enabled(state):
                result.append(action)
        return result

    def result(self, state: State, action: Action) -> State:
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        return action.execute(state)

    def goal_test(self, state: State) -> bool:
        """Return True if the state is a goal."""
        return state.is_goal()

    def path_cost(self, c: int, state1: State, action: Action, state2: State) -> int:
        """Return the cost of a solution path that arrives at state2 from
        state1 via action, assuming cost c to get up to state1. If the problem
        is such that the path doesn't matter, this function will only look at
        state2. If the path does matter, it will consider c and maybe state1
        and action. The default method costs 1 for every step in the path."""
        return c + 1

    def is_valid(self, state: State) -> bool:
        """Method repOK that returns a boolean depending if the state is a valid state."""
        return state.is_valid()
    
    def factory(self):
        raise NotImplementedError

 

class ProblemDecorator:
    def __init__(self, problem: Problem):
        self.problem = problem

    def __getattr__(self, name):
        return getattr(self.problem, name)


class StatisticsProblemDecorator(ProblemDecorator):
    def __init__(self, problem: Problem):
        super().__init__(problem)
        self.generated_nodes = 1
        self.visited_ones = 0
        self.max_nodes_in_frontier = 1

    def __repr__(self):
        return self.problem.__repr__()

    @property
    def no_leaf_nodes(self) -> int:
        return self.visited_ones - 1

    def average_branching_factor(self) -> float:
        if self.no_leaf_nodes == 0:
            return 0
        return (self.generated_nodes - 1) / self.no_leaf_nodes

    def actions(self, state: State) -> list[Action]:
        enabled_actions = self.problem.actions(state)
        return enabled_actions

    def nodes_in_frontier(self) -> int:
        return self.generated_nodes - self.visited_ones

    def result(self, state: State, action: Action) -> State:
        self.generated_nodes += 1
        self.max_nodes_in_frontier = max(
            self.max_nodes_in_frontier, self.nodes_in_frontier()
        )
        return self.problem.result(state, action)

    def goal_test(self, state: State) -> bool:
        self.visited_ones += 1
        return self.problem.goal_test(state)

    def is_valid(self, state: State) -> bool:
        return self.problem.is_valid(state)

    def reset(self) -> None:
        self.generated_nodes = 1
        self.visited_ones = 0
        self.max_nodes_in_frontier = 1
        self.no_leaf_nodes = 0

    def inverse(self):
        return StatisticsProblemDecorator(self.problem.inverse())
