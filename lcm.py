from datetime import datetime
import numpy as np


M = 1038071920
a = 106
b = 0.21132 * M


def get_generator(initial_number=None):

    # только в случае, когда входное значение отсутствует, сами генерируем первое случайное число
    if initial_number == None:
        initial_number = _get_initial_number()
        print(initial_number)
    else:
        print(initial_number)
        initial_number = initial_number * datetime.now().microsecond * datetime.now().second * datetime.now().minute

    if not isinstance(initial_number, int):
        raise ValueError("Входное значение не является числом!")

    while True:
        initial_number = ((a * initial_number) + b) % M
        yield initial_number


def _get_initial_number():

    now = datetime.now().microsecond * datetime.now().second * datetime.now().minute
    return now


def get_values_lcm(seed=None, size=1, maxValue=100):
    generator = get_generator(seed)
    values = []

    for index, value in (zip(range(size), generator)):
        values.append(value)

    if maxValue == 1:
        return np.array(values) % 10000 / 10000
    return np.array(values) % maxValue
