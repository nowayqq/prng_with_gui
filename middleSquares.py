from datetime import datetime
import numpy as np


def get_generator(initial_number=None):
    """
        Генератор случайной последовательности.
        Реализован на основе метода срединных квадратов.
    """
    # только в случае, когда входное значение отсутствует, сами генерируем первое случайное число
    if initial_number == None:
        initial_number = _get_initial_number()

    if not isinstance(initial_number, int):
        raise ValueError("Входное значение не является числом!")

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
    """
        Возвращает количество миллисекунд в текущей дате для построения случайных чисел
    """
    now = datetime.now()
    return now.microsecond


def get_values_ms(seed=None, size=1, maxValue=1):
    generator = get_generator(seed)
    values = []

    for index, value in (zip(range(size), generator)):
        values.append(value)

    return np.array(values) % maxValue
