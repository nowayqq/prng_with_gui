from datetime import datetime
import numpy as np


def get_generator(initial_number=None):
    if initial_number == None or initial_number % 4 != 0:
        initial_number = _get_initial_number()

    if not isinstance(initial_number, int):
        raise ValueError("Входное значение не является числом!")

    print(initial_number)

    while True:
        initial_number = str(initial_number)
        l = len(initial_number)

        initial_number = int(initial_number[2:] + initial_number[0:2]) + int(initial_number[-2:] + initial_number[0:-2])

        if l != len(str(initial_number)):
            yield int(str(initial_number)[-l:])
        yield initial_number


def _get_initial_number():
    now = datetime.now().microsecond * datetime.now().second
    while now % 4 != 0:
        now = datetime.now().microsecond * datetime.now().second
    return now


def get_values_mix(seed=None, size=1, maxValue=100):
    generator = get_generator(seed)
    values = []

    for index, value in (zip(range(size), generator)):
        values.append(value)

    if maxValue == 1:
        return np.array(values) % 10000 / 10000
    return np.array(values) % maxValue
