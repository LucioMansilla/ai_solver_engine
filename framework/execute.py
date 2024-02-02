import signal

from engine.core.engine import Engine
from engine.core.solution import NullSolution
from constants import HEURISTIC_FACTORIES, INFORMED_ALGORITHMS, UNINFORMED_ALGORITHMS

from framework.factories.state_factory import StateFactory
from framework.filemanager.solution_file_manager import SolutionFileManager
from framework.filemanager.state_file_manager import StateFileManager
from framework.parser import framework_parser


def normal_report(args):
    solutions = []
    states = StateFactory.create_from_csv(args.problem, args.input)
    for problem_name, state in states:
        solutions += run(
            problem_name, state, [args.algorithm], args.timelimit, args.heuristics
        )

    SolutionFileManager.write_to_csv(solutions, args.output)
    return solutions


def exhaustive_report(args):
    solutions = []
    print("Starting exhaustive report...")

    states = StateFileManager.create_from_csv(args.input)

    for problem_name, state in states:
        print(f"Running {problem_name} on {state}")
        solutions += run(
            problem_name, state, UNINFORMED_ALGORITHMS.keys(), args.timelimit
        )
        solutions += run(
            problem_name,
            state,
            INFORMED_ALGORITHMS.keys(),
            args.timelimit,
            HEURISTIC_FACTORIES[problem_name].heuristic_names(),
        )

    SolutionFileManager.write_to_csv(solutions, args.output)
    return solutions


def timeout_handler(sigma, frame):
    raise Exception("Time Out!")


def try_solve(engine, time, solutions):
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(time)
    try:
        solution = engine.solve()
        print(solution)
        if solution is not None:
            solutions.append(solution)
    except Exception as e:
        s = NullSolution(
            algorithm=engine.algorithm,
            problem=engine.problem,
            heuristic=engine.heuristic,
            run_time=time,
            params=engine.params,
        )
        solutions.append(s)
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


def run(problem_name, state, algorithms, time, heuristics=None):
    solutions = []
    for algorithm in algorithms:
        if heuristics:
            for heuristic in heuristics:
                e = Engine([problem_name, state], algorithm, heuristic)
                try_solve(e, time, solutions)
        else:
            e = Engine([problem_name, state], algorithm)
            try_solve(e, time, solutions)
    return solutions


def check_exhaustive_parsers(args):
    if args.problem:
        raise Exception(
            "Illegal Argument: Can't use --problem flag with --exhaustive flag"
        )
    if args.algorithm:
        raise Exception(
            "Illegal Argument: Can't use --algorithm flag with --exhaustive flag"
        )
    if args.heuristics:
        raise Exception(
            "Illegal Argument: Can't use --heuristic flag with --exhaustive flag"
        )


def check_normal_parsers(args):
    if not args.input:
        raise Exception("Illegal Argument: --input flag must be specified.")
    if not args.problem:
        raise Exception("Illegal Argument: --problem flag must be specified.")
    if not args.algorithm:
        raise Exception("Illegal Argument: --algorithm flag must be specified.")
    if not args.output:
        raise Exception("Illegal Argument: --output flag must be specified.")


if __name__ == "__main__":
    args = framework_parser()
    if args.exhaustive:
        check_exhaustive_parsers(args)
        exhaustive_report(args)
    else:
        check_normal_parsers(args)
        normal_report(args)
