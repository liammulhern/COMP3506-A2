from structures.m_extensible_list import ExtensibleList

from typing import Any

class MinHeapNode:
    def __init__(self, key: Any, data: Any) -> None:
        self._key = key
        self._data = data

    def __lt__(self, other: 'MinHeapNode') -> bool:
        return self._key < other._key
    
    def __eq__(self, other: 'MinHeapNode') -> bool:
        return self._key == other._key

    def __gt__(self, other: 'MinHeapNode') -> bool:
        return self._key > other._key
    

class MinHeap:
    def __init__(self) -> None:
        self._list = ExtensibleList()

    def get_min(self) -> Any | None:
        if self.is_empty():
            return None

        return self._list[0]

    def insert(self, key: Any, data: Any) -> None:
        node: MinHeapNode = MinHeapNode(key, data)

        self._list.append(node)
        self._up_heap()

    def remove_min(self) -> Any | None:
        if self.is_empty():
            return None

        size: int = self._list.get_size()

        # Replace the root with the last node
        self._list[0] = self._list[size - 1]

        # Remove the last node
        node: MinHeapNode = self._list.remove_at(size - 1)
        self._down_heap(0)

        return node

    def _up_heap(self) -> None:
        current_index: int = self.get_size() - 1

        while current_index > 0:
            parent_node: MinHeapNode | None =  self._get_parent_node(current_index)

            if parent_node is None:
                break

            if parent_node <= self._list[current_index]:
                break

            parent_index: int = self._get_parent_index(current_index)
            self._swap_nodes(parent_index, current_index)

            current_index = parent_index 

    def _down_heap(self, start_index: int) -> None:
        if self.is_empty():
            return

        current_index: int = start_index

        while True:
            left_index: int = self._get_left_index(current_index)

            if left_index > self.get_size() - 1:
                break
            
            least_index: int = left_index
            right_index: int = self._get_right_index(current_index)

            if right_index < self.get_size() - 1 \
                    and self._list[right_index] < self._list[left_index]:

                least_index = right_index

            current_node = self._list[current_index]
            least_node = self._list[least_index]

            if current_node < least_node:
                self._swap_nodes(current_index, least_index)
                current_index = least_index
            else:
                break

    def _swap_nodes(self, index_1: int, index_2: int) -> None:
        temp: MinHeapNode = self._list[index_1] 

        self._list[index_1] = self._list[index_2]
        self._list[index_2] = temp

    def get_size(self) -> int:
        return self._list.get_size()
    
    def is_empty(self) -> bool:
        return self._list.is_empty()

    def _get_parent_index(self, index: int) -> int:
        parent_index: int = (index - 1) // 2

        return parent_index

    def _get_parent_node(self, index: int) -> MinHeapNode | None:
        parent_index: int = self._get_parent_index(index)

        if parent_index < 0:
            return None

        return self._list[parent_index]

    def _get_left_index(self, index: int) -> int:
        left_index: int = (2 * index) + 1

        return left_index 

    def _get_left_node(self, index: int) -> MinHeapNode | None:
        left_index: int = self._get_left_index(index)

        if left_index > self.get_size() - 1:
            return None

        return self._list[left_index]

    def _get_right_index(self, index: int) -> int:
        right_index: int = (2 * index) + 2

        return right_index

    def _get_right_node(self, index: int) -> MinHeapNode | None:
        right_index: int = self._get_right_index(index)

        if right_index > self.get_size() - 1:
            return None

        return self._list[right_index]