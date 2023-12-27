#!/usr/bin/env python3
"""
 Discription - return range to paginate
"""
from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    if type(page) and type(page_size) != int:
        return "<page> and <page_size> must be of type int"

    start = (page - 1) * page_size
    
    if type(start) != int:
        return "First index must be of type int"
    
    end = start + page_size

    if type(start) != int:
        return "Last index must be of type int"
    
    return (start, end)
