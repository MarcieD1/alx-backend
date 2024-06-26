#!/usr/bin/env python3
"""
Module for LFUCache class that inherits from BaseCaching.
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class that inherits from BaseCaching and is a caching system.
    Implements LFU caching algorithm.
    """

    def __init__(self):
        """
        Initialize the class.
        """
        super().__init__()
        self.usage_counts = {}
        self.lru_order = {}

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data the item value for the key key.
        If key or item is None, this method should not do anything.
        Implements LFU algorithm.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.usage_counts[key] += 1
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    self.discard()
                self.cache_data[key] = item
                self.usage_counts[key] = 1
            self.lru_order[key] = self.current_order()
    
    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data, return None.
        """
        if key is None or key not in self.cache_data:
            return None
        self.usage_counts[key] += 1
        self.lru_order[key] = self.current_order()
        return self.cache_data[key]

    def discard(self):
        """
        Discard the least frequently used item in the cache.
        If there is more than one, discard the least recently used.
        """
        least_used = min(self.usage_counts.values())
        candidates = [k for k, v in self.usage_counts.items() if v == least_used]
        if len(candidates) > 1:
            # If more than one candidate, use LRU to decide
            lru_candidate = min(candidates, key=lambda k: self.lru_order[k])
            self.actual_discard(lru_candidate)
        else:
            self.actual_discard(candidates[0])

    def actual_discard(self, key):
        """
        Helper function to actually perform the discard operation.
        """
        print(f"DISCARD: {key}")
        del self.cache_data[key]
        del self.usage_counts[key]
        del self.lru_order[key]

    def current_order(self):
        """
        Generate a unique order value for LRU tracking.
        """
        return max(self.lru_order.values(), default=0) + 1
