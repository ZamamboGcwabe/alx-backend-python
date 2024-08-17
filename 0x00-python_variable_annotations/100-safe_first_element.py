#!/usr/bin/python3
"""
Task 10
"""

from typing import Sequence, Any, Union, Optional

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    if lst:
        return lst[0]
    else:
        return None
