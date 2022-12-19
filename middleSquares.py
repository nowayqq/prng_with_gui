from datetime import datetime
import numpy as np


def get_generator(initial_number=None):

    if initial_number == None:
        initial_number = _get_initial_number()

    if not isinstance(initial_number, int):
        raise ValueError("Входное значение не является числом!")

    print('Seed is ' + str(initial_number))

    while True:
        square_str = str(initial_number ** 2)
        while True:
            if len(square_str) >= 12:
                break
            square_str = "0" + square_str
            if len(square_str) >= 12:
                break
            square_str = square_str + "0"

        initial_number = int(square_str[3:9])
        yield initial_number


def _get_initial_number():

    now = datetime.now()
    return now.microsecond


def get_values_ms(seed=None, size=1, maxvalue=100):

    generator = get_generator(seed)
    values = []

    for index, value in (zip(range(size), generator)):
        values.append(value)

    if maxvalue == 1:
        return np.array(values) % 10000 / 10000
    return np.array(values) % maxvalue
