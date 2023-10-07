"""
COMP3506/7505 S2 2023
The University of Queensland

NOTE: This file will be used for marking.
"""

from typing import Any

from structures.m_entry import *
from structures.m_doubly_linked_list import DoubleLinkedList 
from structures.m_doubly_linked_list import DoubleNode 

class PriorityQueueNode(DoubleNode):
    def __init__(self, priority: int, data: Any) -> None:
        self._priority = priority
        super().__init__(data)

    def get_priority(self) -> int:
        """
        Get the priority of a node.
        """
        return self._priority
    
    def __lt__(self, node: 'PriorityQueueNode') -> bool:
        """
        Compare if a node's priority is less than another.
        NOTE: 0 is the highest priority
        """
        return self._priority > node._priority

    def __eq__(self, node: 'PriorityQueueNode') -> bool:
        """
        Compare if a node has the same priority as another.
        """
        return self._priority == node._priority

    def __str__(self) -> str:
        return f"{self._priority}:{self._data}" 

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
        self._list = DoubleLinkedList()

    def __str__(self) -> str:
        return str(self._list)

    # Warning: This insert() signature changed as of skeleton 1.1, previously
    # the priority and data arguments were switched
    def insert(self, priority: int, data: Any) -> None:
        """
        Insert some data to the queue with a given priority.
        Hint: FIFO queue can just always have the same priority value, no
        need to implement an extra function.
        """
        node: PriorityQueueNode = PriorityQueueNode(priority, data)

        cur = self._list.get_head()
        has_inserted = False

        while cur is not None:
            if node > cur:
                self._list.insert_before(cur, node)
                has_inserted = True
                break
            
            cur = cur.get_next()

        if not has_inserted:
            self._list.insert_to_back(node)

    def insert_fifo(self, data: Any) -> None:
        """
        UPDATE in Skeleton v2.2: Allows a user to add data for FIFO queue
        operations. You may assume a user will NOT mix insert() and
        insert_fifo() - they will either use one all of the time, or the
        other all of the time.
        """
        node: PriorityQueueNode = PriorityQueueNode(0, data)
        self._list.insert_to_back(node)

    def get_min(self) -> Any:
        """
        Return the highest priority value from the queue, but do not remove it
        """
        node: PriorityQueueNode = self._list.get_head()

        return node.get_data() 
        
    def remove_min(self) -> Any:
        """
        Extract (remove) the highest priority value from the queue.
        You must then maintain the queue to ensure priority order.
        """
        node: PriorityQueueNode = self._list.remove_from_front()

        return node.get_data()

    def get_size(self) -> int:
        return self._list.get_size()

    def is_empty(self) -> bool:
        return self._list.is_empty()