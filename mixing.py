from datetime import datetime
import numpy as np


def get_generator(initial_number=None):

    if initial_number is None:
        initial_number = _get_initial_number()

    if not isinstance(initial_number, int):
        raise ValueError("The input value is not a number!")

    print('Seed is ' + str(initial_number))

    if len(str(initial_number)) < 4:
        mod = 4 // len(str(initial_number))
        mod += 1
        initial_number = str(initial_number)
        for i in range(mod):
            initial_number += str(int(initial_number) ** 2)

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


def get_values_mix(seed=None, size=1, maxvalue=1):

    generator = get_generator(seed)
    values = []

    for index, value in (zip(range(size), generator)):
        values.append(value)

    if maxvalue == 1:
        return np.array(values) % 10000 / 10000
    return np.array(values) % maxvalue
