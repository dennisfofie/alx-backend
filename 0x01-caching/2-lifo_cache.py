#!/usr/bin/python3
"""
 Implementing the lifo caching policy algorithm
"""
from collections import OrderedDict
from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """ Detail implementation of the LIFO caching policy
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

        if len(self.cache_data) + 1 > self.MAX_ITEMS:
            first_key , value = self.cache_data.popitem(last=True)
            print("DISCARD: {}".format(first_key))
        
        self.cache_data[key] = item
        self.cache_data.move_to_end(key,True)

    def get(self, key):
       """ retrieve item in the cache
       """
       if not key or None == key:
          return None
       return self.cache_data.get(key)