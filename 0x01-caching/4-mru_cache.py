#!/usr/bin/env python3
"""
Module for MRUCache class that inherits from BaseCaching.
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that inherits from BaseCaching and is a caching system.
    Implements MRU caching algorithm.
    """

    def __init__(self):
        """
        Initialize the class.
        """
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data the item value for the key key.
        If key or item is None, this method should not do anything.
        Implements MRU algorithm.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_order.remove(key)
            self.cache_data[key] = item
            self.cache_order.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded_key = self.cache_order.pop(-2)  # MRU except the last added
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data, return None.
        """
        if key is None or key not in self.cache_data:
            return None
        self.cache_order.remove(key)
        self.cache_order.append(key)
        return self.cache_data[key]
