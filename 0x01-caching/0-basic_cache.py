#!/usr/bin/python3
""" Implement caching algorithm in python
"""

from base_caching import BaseCaching
from typing import Any

class BasicCache(BaseCaching):
    """ The caching class detail implementation
    """

    def __init__(self):
        super().__init__()
    
    def put(self, key, item) -> None:
        """ Add item to the cache
        """
        if key or item is not None:
            self.cache_data[key] = item
    
    def get(self, key) -> Any:
        """ Retrieve cache item from the cache system
        """
        if not key or key is None:
            return None
        return self.cache_data.get(key)