# Caching Systems

This repository contains implementations of various caching algorithms, including Least Recently Used (LRU), Most Recently Used (MRU), and Least Frequently Used (LFU) caching mechanisms. These implementations are designed to demonstrate the core principles of caching systems and their behavior in different scenarios.

## Description

The caching systems are implemented in Python and inherit from a base class `BaseCaching`, which provides the basic structure and interface for a caching system. Each caching algorithm overrides specific methods to implement its unique strategy for storing and retrieving items from the cache.

### Files

- `base_caching.py`: Contains the `BaseCaching` class, which defines the basic structure of a caching system.
- `4-mru_cache.py`: Implements the Most Recently Used (MRU) caching algorithm.
- `100-lfu_cache.py`: Implements the Least Frequently Used (LFU) caching algorithm, with a tie-breaker using the Least Recently Used (LRU) strategy for items with the same usage frequency.

## Usage

To use the caching systems, you can import the desired cache class from its file and interact with it through its `put` and `get` methods.

### Example

```python
from mru_cache import MRUCache

my_cache = MRUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
print(my_cache.get("A"))  # Output: Hello
my_cache.put("C", "Holberton")
my_cache.print_cache()
```

Replace `MRUCache` with `LFUCache` to use the Least Frequently Used caching system.

## Requirements

- Python 3.6 or later.

## Running the Tests

Each caching system comes with a main file that demonstrates its behavior and can be used as a basic test. For example, to test the MRU cache, you can run:

```bash
./4-main.py
```

Replace `4-main.py` with `100-main.py` to test the LFU cache.

## Contributing

Contributions to this project are welcome. Please ensure that your code adheres to the project's coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
```

