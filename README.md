# Artificial Intelligence Project

---

This is an AI project, made by [Lucio Mansilla](https://github.com/LucioMansilla), [Brenda Dichiara](https://github.com/BrendaDichiara) and [Valentín Buttignol](https://github.com/ValenButtignol), students of the National University of Río Cuarto ([UNRC](https://www.unrc.edu.ar/)). The objective with this project is to make an easy to use framework for Search Problems.

The project consists in an [AimaCode](https://github.com/aimacode/aima-python) based Engine for running algorithms with different problems, and a State Generator for those problems. So we have made a framework that uses the engine with the programmed problems, search algorithms and heuristics.

---

## Algorithms, Problems and Heuristics

As we said earlier, this repository is based on the [AimaCode](https://github.com/aimacode/aima-python) schema, which, in turn, is based on the structure imposed by Stuart Russell and Peter Norvig in [Artificial Intelligence: A Moddern Approach](https://www.amazon.com/Artificial-Intelligence-Modern-Approach-3rd/dp/0136042597)

The structure of this repository was intended to be scalable, in terms of the types of problems that can be considered part of learning AI programming. For this reason, so far, the project includes the following algorithms:

### Uninformed Algorithms

- [Depth First Search](https://github.com/IA-UNRC-2023/tp1-dichiara-mansilla-buttignol/blob/main/engine/algorithms/uninformed/depth_first_search.py#L6)
- [Depth First Acyclic Search](https://github.com/IA-UNRC-2023/tp1-dichiara-mansilla-buttignol/blob/main/engine/algorithms/uninformed/depth_first_search.py#L34) (Efficient variant of regular Depth First Search)
- [Depth First Visited Search](https://github.com/IA-UNRC-2023/tp1-dichiara-mansilla-buttignol/blob/main/engine/algorithms/uninformed/depth_first_search.py#L17) (Efficient variant of regular Depth First Search)
- [Breadth First Search](https://github.com/IA-UNRC-2023/tp1-dichiara-mansilla-buttignol/blob/main/engine/algorithms/uninformed/breadth_first_search.py#L22) (Efficient variant of regular Breadth First Search)
- [Breadth First Acyclic Search](https://github.com/IA-UNRC-2023/tp1-dichiara-mansilla-buttignol/blob/main/engine/algorithms/uninformed/breadth_first_search.py#L33) (Efficient variant of regular Breadth First Search)
- [Breadth First Visited Search](https://github.com/IA-UNRC-2023/tp1-dichiara-mansilla-buttignol/blob/main/engine/algorithms/uninformed/breadth_first_search.py#L7) (Efficient variant of regular Breadth First Search)
- [Depth Limited Search](https://github.com/IA-UNRC-2023/tp1-dichiara-mansilla-buttignol/blob/main/engine/algorithms/uninformed/depth_limited_search.py#L6)
- [Iterative Deepening](https://github.com/IA-UNRC-2023/tp1-dichiara-mansilla-buttignol/blob/main/engine/algorithms/uninformed/iterative_deepening.py#L7)
- [Uniform Cost Search](https://github.com/IA-UNRC-2023/tp1-dichiara-mansilla-buttignol/blob/main/engine/algorithms/uninformed/uniform_cost_search.py#L4)
- [Bidirectional Search](https://github.com/IA-UNRC-2023/tp1-dichiara-mansilla-buttignol/blob/main/engine/algorithms/uninformed/bidirectional_search.py#L7)

### Informed Algorithms
- [Greedy Best First Search](https://github.com/IA-UNRC-2023/tp1-dichiara-mansilla-buttignol/blob/main/engine/algorithms/informed/greedy_best_first_search.py#L8)
- [A* Search](https://github.com/IA-UNRC-2023/tp1-dichiara-mansilla-buttignol/blob/main/engine/algorithms/informed/astar_search.py)

For this algorithms we've programmed different problems, defining certain rules and actions for each problem. Also, for Informed Algorithms, we've programmed different heuristics for each problem.

### Problems and Heuristics

- [N-Puzzle](https://github.com/IA-UNRC-2023/tp1-dichiara-mansilla-buttignol/blob/main/engine/problems/n_puzzle.py)
  - [Euclidean Distance](https://github.com/IA-UNRC-2023/tp1-dichiara-mansilla-buttignol/blob/main/engine/heuristics/n_puzzle_heuristics.py#L59)
  - [Gaschnig Heuristic](https://github.com/IA-UNRC-2023/tp1-dichiara-mansilla-buttignol/blob/main/engine/heuristics/n_puzzle_heuristics.py#L33)
  - [Incorrect Placed Squares](https://github.com/IA-UNRC-2023/tp1-dichiara-mansilla-buttignol/blob/main/engine/heuristics/n_puzzle_heuristics.py#L4)
  - [Manhattan Distance](https://github.com/IA-UNRC-2023/tp1-dichiara-mansilla-buttignol/blob/main/engine/heuristics/n_puzzle_heuristics.py#L19)
- [N-Queens](https://github.com/IA-UNRC-2023/tp1-dichiara-mansilla-buttignol/blob/main/engine/problems/n_queens.py)
  - [Count Conflicted Queens](https://github.com/IA-UNRC-2023/tp1-dichiara-mansilla-buttignol/blob/main/engine/heuristics/n_queens_heuristics.py#L4)
- [Romania Map Problem](https://github.com/IA-UNRC-2023/tp1-dichiara-mansilla-buttignol/blob/main/engine/problems/romania.py)
  - [Euclidean Distance](https://github.com/IA-UNRC-2023/tp1-dichiara-mansilla-buttignol/blob/main/engine/heuristics/romania_heuristics.py#L5)

---

## Usage

As we mentioned in the beggining, with this framework we can generate mixed or hard states, and we can execute the algorithms. The idea is to use ```csv``` files as inputs and outputs, so we can have a record of the accumulated data of each execution.

### Commands

**For generate initial states, execute this in the terminal:**

```
python3 -m framework.generate -p <problem_name> <parameter> -o <output> -n <amount_of_states> -m <generation_mode> -t <time_limit> -aw <writing_file_mode>
```

Where:

```
Necesary:
<problem_name> = 'NPuzzle' | 'NQueens' | 'Romania'
<parameter>
<output>
```

```
Optionals:
<amount_of_states> = 0 | ... | 100 (Default 50)
<generation_mode> = 'mix' | 'hard' (Default = mix)
<time_limit> = 0 | ... | 100 (Default 50)
<writing_file_mode> = 'a' | 'w' (Default = a)
```

**For running an exhaustive output:**

```
python3 -m framework.execute -e -i <input> -o <output>
```

**For running a normal output:**

```
python3 -m framework.execute -p <problem_name> -a <algorithms> -hf <heuristic_functions> -i <input> -o <output>  -t <time_limit> -aw <writing_file_mode>
```

Where:

```
Necesary:
<problem_names> = 'NPuzzle' | 'NQueens' | 'Romania'
<algorithms> = 'BestFirstSearch' | 'A*' | 'DepthFirstSearch' | 'BreadthFirstSearch' | 'DepthFirstVisitedSearch' | 'BreadthFirstVisitedSearch' | 'UniformCostSearch' | 'BidirectionalSearch' | 'IterativeDeepeningSearch'
<heuristic_functions> = 'Gaschnig' | 'IncorrectPlacedSquares' | 'ManhattanDistance' | 'CountConflictedQueens' | 'EuclideanDistance'
<input>
<output>
```

```
Optionals::
<time_limit> = 0 | ... | 100 (Default 50)
<writing_file_mode> = 'a' | 'w' (Default = a)
```

### Notices

- The file generated with the state generator, will follow a ```Problem, State``` syntax. This is because we will want to generate the states, and then execute them as inputs.
- The file generated with the state generator, will be stored in this directory: ```framework/storage/generated_states```
- You can append states of different problems to the file generated with the state generator. This is useful when you want to execute in exhaustively mode. 
- The file of problems to execute, will follow a ```Problem Name, Params, Algorithm, Heuristic, Initial State, Final State, Path, Path Cost, Action Sequence, Run Time, Memory Used, Depth, Branching Factor, Generated Nodes, Visited Nodes, Max Nodes in Frontier, No Leaf Nodes, Brute Memory``` syntax, so we can compare different solutions of different states.
- The file of problems to execute, will be stored in this directory: ```framework/storage/outputs``` .
- The mixed mode, generates 5 times the amount of states argumented; and selects 20% of the amount of easiest states generated, 20% of the hardests and the rest is randomly selected.
- The hard mode, generates 10 times the amount of states argumented; and selects the hardests ones.

---

## Disclaimer

- When executing a normal output, if the heuristic doesn't fit to the problem, an exception is raised.
- Bidirectional search can't be executed with N-Queens Problem because it isn't a reversible problem due to the quantity of amount of final states (is greater than 1).
- When executing a exhaustive output, be aware of the time limit parameter. It can cause an excessive usage of memory.
- You can execute only one algorithm for problem with the normal output, but you can use multiple heuristics (If you use informed search).
- For generating states, you need to specify the problem parameter for N-Queens and N-Puzzle. The parameter would be the specific type of problem, for example, 3-Puzzle, 8-Puzzle, etc.
- Yoy must specify the ```csv``` extension in args.
# ai_solver_engine
