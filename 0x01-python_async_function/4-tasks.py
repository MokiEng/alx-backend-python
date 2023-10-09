#!/usr/bin/env python3
"""a module that create asyncio tasks."""
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list:
    """
    Run wait_n(n, max_delay) concurrently using asyncio.Tasks.

    Args:
        n (int): Number of times to call wait_random.
        max_delay (int): The maximum delay for wait_random.

    Returns:
        list: List of delays from wait_random.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*tasks)
