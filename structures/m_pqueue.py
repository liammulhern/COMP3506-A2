"""
COMP3506/7505 S2 2023
The University of Queensland

NOTE: This file will be used for marking.
"""

from typing import Any

from structures.m_entry import *


class PriorityQueue:
    """
    An implementation of the PriorityQueue ADT.
    The provided methods consume keys and values. Keys are called "priorities"
    and should be integers in the range [0, n] with 0 being the highest priority.
    Values are called "data" and store the payload data of interest.
    For convenience, you may wish to also implement the functionality provided in
    terms of the Entry type, but this is up to you.
    """
    
    def __init__(self):
        """
        Construct the priority queue.
        You are free to make any changes you find suitable in this function to initialise your pq.
        """
        # IMPLEMENT ME!
        pass

    # Warning: This insert() signature changed as of skeleton 1.1, previously
    # the priority and data arguments were switched
    def insert(self, priority: int, data: Any) -> None:
        """
        Insert some data to the queue with a given priority.
        Hint: FIFO queue can just always have the same priority value, no
        need to implement an extra function.
        """
        # IMPLEMENT ME!
        pass

    def insert_fifo(self, data: Any) -> None:
        """
        UPDATE in Skeleton v2.2: Allows a user to add data for FIFO queue
        operations. You may assume a user will NOT mix insert() and
        insert_fifo() - they will either use one all of the time, or the
        other all of the time.
        """
        # IMPLEMENT ME!
        pass

    def get_min(self) -> Any:
        """
        Return the highest priority value from the queue, but do not remove it
        """
        # IMPLEMENT ME!
        pass

    def remove_min(self) -> Any:
        """
        Extract (remove) the highest priority value from the queue.
        You must then maintain the queue to ensure priority order.
        """
        # IMPLEMENT ME!
        pass

    def get_size(self) -> int:
        # IMPLEMENT ME!
        pass

    def is_empty(self) -> bool:
        # IMPLEMENT ME!
        pass
