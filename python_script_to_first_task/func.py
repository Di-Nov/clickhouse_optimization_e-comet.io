import time
import random
from logger import logger
import functools


def time_meter(function):
    @functools.wraps(function)
    def wrapper(*args):
        start = time.time()
        res = function(*args)
        end = time.time()
        logger.info(f"Execution time {end - start} seconds in {function.__name__} function")
        return res

    return wrapper


nums_2 = [random.randrange(-100, 100) for _ in range(10 ** 7)]


@time_meter
def t(nums: list[int]) -> list[int]:
    result = list(map(lambda x: x ** 2, filter(lambda x: x > 0, nums)))
    return result


@time_meter
def n(nums: list[int]) -> list[int]:
    return [x ** 2 for x in nums if x > 0]


t(nums_2)
n(nums_2)
