#!/usr/bin/env python3
"""A Basic Caching Module."""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Representing an object that allows storing and
    retrieving items from a dictionary."""
    def put(self, key, item):
        """It adds an item in the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Then, retrieves an item by key."""
        return self.cache_data.get(key, None)
