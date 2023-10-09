#!/usr/bin/env python3
"""a module Import wait_random from 0-basic_async_syntax."""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio.Task for wait_random(max_delay).

    Args:
        max_delay (int): The maximum delay for wait_random.

    Returns:
        asyncio.Task: A Task that runs wait_random(max_delay).
    """
    return asyncio.create_task(wait_random(max_delay))
