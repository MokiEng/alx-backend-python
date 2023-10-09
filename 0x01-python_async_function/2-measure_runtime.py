#!/usr/bin/env python3
"""time module to measure an approximate elapsed time."""
from asyncio import run
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns total_time / n.

    Args:
        n (int): The number of times to run wait_n.
        max_delay (int): The maximum delay for each
        wait_random call in wait_n.

    Returns:
        float: The average execution time per call.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n
