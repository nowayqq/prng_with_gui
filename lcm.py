from datetime import datetime
import numpy as np


M = 3385574415
a = 106
b = 1283


def get_generator(initial_number=None):

    if initial_number is None:
        initial_number = _get_initial_number()
    print('Seed is ' + str(initial_number))

    if not isinstance(initial_number, int):
        raise ValueError("The input value is not a number!")

    while True:
        initial_number = ((a * initial_number) + b) % M
        yield initial_number


def _get_initial_number():

    return datetime.now().microsecond * datetime.now().second * datetime.now().minute


def get_values_lcm(seed=None, size=1, maxvalue=1):

    generator = get_generator(seed)
    values = []

    for index, value in (zip(range(size), generator)):
        values.append(value)

    if maxvalue == 1:
        return np.array(values) % 10000 / 10000
    return np.array(values) % maxvalue
