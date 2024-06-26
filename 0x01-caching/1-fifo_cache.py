#!/usr/bin/env python3
"""
Module for FIFOCache class that inherits from BaseCaching.
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class that inherits from BaseCaching and is a caching system.
    Implements FIFO caching algorithm.
    """

    def __init__(self):
        """
        Initialize the class.
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data the item value for the key key.
        If key or item is None, this method should not do anything.
        Implements FIFO algorithm.
        """
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    discarded_key = self.keys.pop(0)
                    del self.cache_data[discarded_key]
                    print(f"DISCARD: {discarded_key}")
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data, return None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
