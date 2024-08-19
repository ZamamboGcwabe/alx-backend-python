#!/usr/bin/env python3
"""
Write an asynchronous coroutine named wait_random that waits for
a random delay between 0 and max_delay seconds and eventually returns it.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Waits for a random number of seconds.
    '''
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
