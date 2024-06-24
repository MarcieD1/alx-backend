#!/usr/bin/env python3
"""
This module defines a simple helper function for pagination.
"""

def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end index for pagination.

    Args:
    page: The current page number.
    page_size: The number of items per page.

    Returns:
    A tuple containing the start index and the end index.
    """
    end_index = page * page_size
    start_index = end_index - page_size
    return (start_index, end_index)
