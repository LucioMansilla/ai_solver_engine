from engine.problems.problem import State


class Node:
    """A node in a search tree. Contains a pointer to the parent (the node
    that this is a successor of) and to the actual state for this node. Note
    that if a state is arrived at by two paths, then there are two nodes with
    the same state. Also includes the action that got us to this state, and
    the total path_cost (also known as g) to reach the node. Other functions
    may add an f and h value; see best_first_graph_search and astar_search for
    an explanation of how the f and h values are handled. You will not need to
    subclass this class."""

    def __init__(
        self,
        state: State = None,
        parent: object = None,
        action: object = None,
        path_cost: int = 0,
    ) -> object:
        """Create a search tree Node, derived from a parent by an action."""
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        return "<Node {}>".format(self.state)

    def __lt__(self, other):
        return self.path_cost < other.path_cost

    def expand(self, problem):
        """List the nodes reachable in one step from this node."""
        possible_actions = []
        result = []
        for action in problem.actions(self.state):
            possible_actions.append(action)
        for action in possible_actions:
            result.append(self.child_node(problem, action))
        return result

    def child_node(self, problem, action):
        next_state = problem.result(self.state, action)
        next_node = Node(
            next_state,
            self,
            action,
            problem.path_cost(self.path_cost, self.state, action, next_state),
        )
        return next_node

    def solution(self):
        """Return the sequence of actions to go from the root to this node."""
        return [node.action for node in self.path()[1:]]

    def path(self):
        """Return a list of nodes forming the path from the root to this node."""
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        # We use the hash value of the state
        # stored in the node instead of the node
        # object itself to quickly search a node
        # with the same state in a Hash Table
        return hash(self.state)

    def __str__(self):
        return (
            f"STATE: {self.state} - ACTION: {self.action} - PATH COST: {self.path_cost}"
            f"PARENT: {self.parent} - DEPTH: {self.depth}"
        )

class SearchTreeNode(Node):
    pass

class LocalSearchNode(Node):
    pass


class NullNode(Node):
    pass

    def __eq__(self, other):
        return isinstance(other, NullNode)

class CutNode(Node):
    pass

    def __eq__(self, other):
        return isinstance(other, CutNode)


null_node = NullNode()
cut_off_node = CutNode()
