import csv
import ast

filename = "framework/storage/generated_states/Prueba.csv"  # Reemplaza esto con el nombre de tu archivo
from engine.core.engine import Engine
import pytest
from constants import (
    INFORMED_ALGORITHMS,
    UNINFORMED_ALGORITHMS,
    HEURISTIC_FACTORIES,
    AVAILABLE_PROBLEMS,
    DUMMY,
    NPUZZLE,
    ROMANIA,
)
from tests.utils_test import utils_test

initial_state_informed = {
    "NPuzzle": (1, 8, 2, 0, 4, 3, 7, 6, 5),
    "NQueens": [4, 4, 3, 2, 1, 5, 6, 7],
    "Romania": ("Arad", "Bucharest"),
}

final_state_informed = {
    "NPuzzle": (1, 2, 3, 4, 5, 6, 7, 8, 0),
    "NQueens": [3, 6, 4, 2, 0, 5, 7, 1],
    "Romania": ("Bucharest", "Bucharest"),
}


def create_engine_config_informed():
    config_informed = []
    for problem_name in AVAILABLE_PROBLEMS:
        for algorithm_name in INFORMED_ALGORITHMS.keys():
            for heuristic_name in HEURISTIC_FACTORIES[problem_name].heuristics.keys():
                if heuristic_name != "NonHeuristic":
                    config_informed.append(
                        (
                            problem_name,
                            initial_state_informed[problem_name],
                            algorithm_name,
                            heuristic_name,
                            final_state_informed[problem_name],
                        )
                    )
    return config_informed


def write_to_csv(cls, solutions, output_file: str, file_mode: str):
    headers = ["Problem Name", "Initial State"]
    with open(output_file, file_mode) as f:
        if f.tell() == 0:
            f.write(",".join(headers) + "\n")
        for s in solutions:
            f.write(f"{s.problem_name},{s.initial_state}\n")


if __name__ == "__main__":
    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(
            reader
        )  # omitimos la primera fila que contiene los nombres de las columnas
        problem_list = []
        for row in reader:
            problem_name = row[0]
            initial_state_str = "".join(
                row[1:]
            )  # unimos los elementos de la lista para obtener la cadena completa
            print(initial_state_str)
            initial_state = ast.literal_eval(initial_state_str)
            problem_list.append((problem_name, initial_state))
        print(problem_list)
