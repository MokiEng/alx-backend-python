#!/usr/bin/env python3
"""a module that create asyncio tasks."""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run wait_n(n, max_delay) concurrently using asyncio.Tasks.

    Args:
        n (int): Number of times to call wait_random.
        max_delay (int): The maximum delay for wait_random.

    Returns:
        list: List of delays from wait_random.
    """
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
