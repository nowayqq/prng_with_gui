from datetime import datetime
import numpy as np


mul = 3521


def get_generator(initial_number=None):

    if initial_number == None:
        initial_number = _get_initial_number()

    if not isinstance(initial_number, int):
        raise ValueError("Входное значение не является числом!")

    print(initial_number)

    while True:
        mul_str = str(initial_number * mul)
        while True:
            if len(mul_str) >= 12:
                break
            mul_str = "0" + mul_str
            if len(mul_str) >= 12:
                break
            mul_str = mul_str + "0"

        initial_number = int(mul_str[3:9])
        yield initial_number


def _get_initial_number():

    now = datetime.now()
    return now.microsecond


def get_values_mm(seed=None, size=1, maxValue=100):
    generator = get_generator(seed)
    values = []

    for index, value in (zip(range(size), generator)):
        values.append(value)

    if maxValue == 1:
        return np.array(values) % 10000 / 10000
    return np.array(values) % maxValue
