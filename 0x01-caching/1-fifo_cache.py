#!/usr/bin/python3
"""
 Implementing the fifo caching policy algorithm
"""
from collections import OrderedDict
from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """ Detail implementation of the FIFO caching policy
    """

    def __init__(self):
        """ Initialize the caching policy
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add item to the cache
        """
        if not key or None is item:
            return
        self.cache_data[key] = item

        if len(self.cache_data) > self.MAX_ITEMS:
            first_key , value = self.cache_data.popitem()
            print("DISCARD: {}".format(first_key))

    def get(self, key):
       """ retrieve item in the cache
       """
       if not key or None == key:
          return None
       return self.cache_data.get(key)