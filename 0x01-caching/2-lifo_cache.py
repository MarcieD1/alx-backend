#!/usr/bin/env python3
"""
Module for LIFOCache class that inherits from BaseCaching.
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class that inherits from BaseCaching and is a caching system.
    Implements LIFO caching algorithm.
    """

    def __init__(self):
        """
        Initialize the class.
        """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data the item value for the key key.
        If key or item is None, this method should not do anything.
        Implements LIFO algorithm.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                if self.last_key:
                    del self.cache_data[self.last_key]
                    print(f"DISCARD: {self.last_key}")
            self.cache_data[key] = item
            self.last_key = key

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data, return None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
