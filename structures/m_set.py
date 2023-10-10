from structures.m_map import Map
from structures.m_entry import Entry
from structures.m_single_linked_list import SingleLinkedList
from structures.m_single_linked_list import SingleNode

from typing import Any

class Set(Map):
    def add(self, key: Any) -> None:
        """
        """
        super().insert_kv(key, 0)

    def __str__(self) -> str:
        size: int = 0
        str_out: str = "{" 

        first_entry = True
        
        for i in range(self._capacity):           
            if self._entry_array[i] is None:
                continue

            if size == self._size:
                break

            if not first_entry:
                str_out += ", "
            else:
                first_entry = False

            entry: Entry = self._entry_array[i]

            str_out += str(entry.get_key())
            size += 1

        str_out += "}"

        return str_out


