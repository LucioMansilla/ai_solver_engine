import argparse
from constants import GENERATED_STATES_PATH, OUTPUTS_PATH


def framework_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p", "--problem", help="Available Problems: NPuzzle, NQueens, RomaniaMap"
    )
    parser.add_argument(
        "-a",
        "--algorithm",
        help="Available Algorithms: BestFirstSearch, A*, DepthFirstSearch, BreadthFirstSearch, DepthFirstVisitedSearch, BreadthFirstVisitedSearch, UniformCostSearch, BidirectionalSearch, IterativeDeepeningSearch",
    )
    parser.add_argument("-hf", "--heuristics", nargs="+")
    parser.add_argument("-i", "--input", help="Name of the Input", required=True)
    parser.add_argument("-o", "--output", help="Name of the output", required=True)
    parser.add_argument(
        "-e", "--exhaustive", help="Exhaustive mode", action="store_true"
    )
    parser.add_argument("-t", "--timelimit", help="Time limit", default=50, type=int)
    parser.add_argument(
        "-aw", "--filemode", help="Opening file mode", default="a", choices=["a", "w"]
    )

    args = parser.parse_args()
    args.input = GENERATED_STATES_PATH + args.input
    args.output = OUTPUTS_PATH + args.output

    return args


def generator_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p",
        "--problem",
        nargs="+",
        help="Available Problems: NPuzzle, NQueens, RomaniaMap",
        required=True,
    )
    parser.add_argument(
        "-n", "--amount", help="Amount of problems", default=50, type=int
    )
    parser.add_argument("-o", "--output", help="Name of the output", required=True)
    parser.add_argument(
        "-m",
        "--mode",
        help="Generation mode: mix, hard",
        default="mix",
        choices=["mix", "hard"],
    )
    parser.add_argument("-t", "--timelimit", help="Time limit", default=50, type=int)
    parser.add_argument(
        "-aw", "--filemode", help="Opening file mode", default="a", choices=["a", "w"]
    )
    args = parser.parse_args()
    args.output = GENERATED_STATES_PATH + args.output

    return args
