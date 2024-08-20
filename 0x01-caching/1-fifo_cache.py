#!/usr/bin/env python3
"""This is First-In First-Out (fifo) caching module."""
from collections import OrderedDict

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """This is a Representaion of an object that allows
    storing andretrieving items from a dictionary with a FIFO
    removal mechanism when the limit is reached."""
    def __init__(self):
        """Initializing the cache."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adding an item to/in the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """Retrieving an item by key*."""
        return self.cache_data.get(key, None)
