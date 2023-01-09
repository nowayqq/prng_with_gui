from datetime import datetime
import numpy as np


def get_generator(initial_number=None):

    if initial_number is None:
        initial_number = _get_initial_number()

    if not isinstance(initial_number, int):
        raise ValueError("The input value is not a number!")

    print('Seed is ' + str(initial_number))

    while True:

        initial_number = str(initial_number)
        if len(initial_number) == 1:
            initial_number *= 2

        if len(initial_number) < 8:
            mod = int(8 / len(initial_number))
            initial_number = int(initial_number)
            for i in range(mod):
                initial_number *= initial_number
        else:
            initial_number = int(initial_number)

        square_str = str(initial_number ** 2)

        initial_number = int(square_str[3:9])
        yield initial_number


def _get_initial_number():

    return datetime.now().microsecond


def get_values_ms(seed=None, size=1, maxvalue=1):

    generator = get_generator(seed)
    values = []

    for index, value in (zip(range(size), generator)):
        values.append(value)

    if maxvalue == 1:
        return np.array(values) % 10000 / 10000
    return np.array(values) % maxvalue
