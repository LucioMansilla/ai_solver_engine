import signal
import random
from constants import BETTER_ALGORITHM, BETTER_HEURISTIC, MULTIPLIER
from engine.core.engine import Engine
from engine.core.solution import Solution
from framework.factories.state_factory import StateFactory
from framework.filemanager.state_file_manager import StateFileManager
from framework.parser import generator_parser


def timeout_handler(sigma, frame):
    raise Exception("Timeout!")


def try_generate(engine, time, solutions):
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(time)
    try:
        solution = engine.solve()
        if solution is not None:
            solutions.append(solution)
    except Exception as e:
        print(
            "----------------------------------------------------------------------------------------------------------------"
        )
        print(
            f"Time out!, the algorithm {engine.algorithm.__class__.__name__} did not find a solution in {time} seconds"
        )
        print(
            "----------------------------------------------------------------------------------------------------------------"
        )
        return
    finally:
        signal.alarm(0)


def filter_solutions(s: list[Solution], m: str, amount: int) -> list[Solution]:
    s.sort(key=lambda x: x.depth)

    if m == "hard":
        return s[-amount:]

    if m == "mix":
        percentage = int(amount * 0.2)
        percentage_random = amount - (percentage * 2)
        result = s[-percentage:] + s[:percentage]

        s = s[percentage:-percentage]
        random.shuffle(s)
        result.extend(s[:percentage_random])

        return result


def run(args):
    states = StateFactory.create(args.problem, args.amount * MULTIPLIER[args.mode])
    solutions = []
    for state in states:
        e = Engine(
            [args.problem[0], state],
            BETTER_ALGORITHM,
            BETTER_HEURISTIC[args.problem[0]],
        )
        try_generate(e, args.timelimit, solutions)
    solutions = filter_solutions(solutions, args.mode, args.amount)
    StateFileManager.write_to_csv(solutions, args.output, args.filemode)


if __name__ == "__main__":
    run(generator_parser())
