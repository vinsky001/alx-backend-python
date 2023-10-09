#!/usr/bin/env python3

"""
Create a measure_time function with integers n and max_delay as arguments
that measures the total execution time for wait_n(n, max_delay), and returns
total_time / n. Your function should return a float.

Use the time module to measure an approximate elapsed time.
"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measures the total execution time for wait_n(n, max_delay), and returns
    total_time / n. Your function should return a float.
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    return (end - start) / n


if __name__ == '__main__':
    print("Execution time: {}".format(measure_time(5, 9)))
