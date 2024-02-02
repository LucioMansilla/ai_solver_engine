from engine.core.solution import Solution
import csv


class StateFileManager:
    @classmethod
    def write_to_csv(cls, solutions: list[Solution], output_file: str, file_mode: str):
        with open(output_file, file_mode, encoding="UTF8", newline="") as f:
            writer = csv.writer(f)
            if f.tell() == 0:
                writer.writerow(["Problem Name", "Initial State"])
            for s in solutions:
                writer.writerow((s.problem_name, s.initial_state))

    @classmethod
    def create_from_csv(cls, file_path: str) -> list[tuple]:
        states = []
        with open(f"{file_path}", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                state = row["Problem Name"], eval(row["Initial State"])
                states.append(state)

        return states
