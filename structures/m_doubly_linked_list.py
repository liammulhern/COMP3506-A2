from structures.m_single_linked_list import SingleNode  
from structures.m_single_linked_list import SingleLinkedList
from typing import Any

class DoubleNode(SingleNode):
    """
    """
    def __init__(self, data: Any) -> None:
        self._prev = None
        super().__init__(data)

    def set_prev(self, node: SingleNode) -> Any:
        self._prev = node

    def get_prev(self) -> SingleNode | None:
        return self._prev

class DoubleLinkedList(SingleLinkedList):
    """
    """
    _head: DoubleNode | None
    _tail: DoubleNode | None

    def insert_to_front(self, node: DoubleNode) -> None:
        if self._head is not None:
            self._head.set_prev(node)

        return super().insert_to_front(node)

    def insert_to_back(self, node: DoubleNode) -> None:
        """
        Insert a node to the back of the list
        """
        # Set the insertion node's previous node to the current tail
        node.set_prev(self._tail)

        super().insert_to_back(node)

    def remove_from_back(self) -> DoubleNode | None:
        """
        Remove and return the front element
        """
        if self._size == 0:
            return None

        node: DoubleNode = self.get_tail()
        self._tail = node.get_prev()

        if self._tail is None:
            self._head = None

        self._size -= 1
        return node

    def insert_after(self, insert_after_node: DoubleNode, node: DoubleNode) -> None:
        """
        Insert a node after the current node and before the next.
        """
        if insert_after_node is self._tail:
            self.insert_to_back(node)
            return

        next: DoubleNode = insert_after_node.get_next()
        node.set_next(next)
        node.set_prev(insert_after_node)
        insert_after_node.set_next(node)
        next.set_prev(node)
        self._size += 1
    
    def insert_before(self, insert_before_node: DoubleNode, node: DoubleNode) -> None:
        """
        Insert a node before the current node and after the previous.
        """
        if insert_before_node is self._head:
            self.insert_to_front(node)
            return

        prev = insert_before_node.get_prev()
        node.set_prev(prev)
        node.set_next(insert_before_node)
        insert_before_node.set_prev(node)
        prev.set_next(node)
        self._size += 1

    def is_empty(self) -> bool:
        """
        Check if the list is empty
        """
        return self._size == 0