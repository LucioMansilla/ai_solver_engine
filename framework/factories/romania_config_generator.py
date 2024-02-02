import random
from framework.filemanager.state_file_manager import StateFileManager
from constants import ROMANIA


class RomaniaConfigGenerator:
    @classmethod
    def create(cls, amount: int) -> list:
        return cls.__generate_valid_config(amount)

    @classmethod
    def create_from_csv(cls, file_path: str) -> list[tuple]:
        states = StateFileManager.create_from_csv(file_path)
        for state in states:
            problem_name = state[0]
            current_state = state[1]
            if problem_name != ROMANIA:
                raise Exception(
                    f"Invalid problem name on input. Expected ROMANIA but got {problem_name}"
                )
            if not cls.__is_valid_state(current_state):
                raise Exception(f"Invalid state on input. Got {current_state}")
        return states

    @classmethod
    def __generate_valid_config(cls, amount: int) -> list:
        from constants import ROMANIA_MAP

        states = set()
        nodes = list(ROMANIA_MAP.nodes())
        result = []

        while len(states) < amount:
            origin = random.choice(nodes)
            destination = random.choice(nodes)
            if origin != destination:
                states.add(tuple((origin, destination)))

        for state in states:
            result.append(state)

        return result

    @classmethod
    def __is_valid_state(cls, tuple: tuple) -> bool:
        from constants import ROMANIA_MAP

        nodes = list(ROMANIA_MAP.nodes())
        if tuple[0] not in nodes or tuple[1] not in nodes:
            return False
        return True
