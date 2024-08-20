#!/usr/bin/env python3
""" Import async_generator then write a coroutine called
async_comprehension that takes no arguments.
"""
from typing import List
from importlib import import_module as usin


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ The coroutine will collect 10 random numbers using an
    async comprehensing over async_generator,
    then return the 10 random numbers.
    """
    return [num async for num in async_generator()]
