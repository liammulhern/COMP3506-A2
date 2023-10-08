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
        """
        Get the printable string representation of the map
        """
        size: int = 0
        str_out: str = "{"

        first_index = True 

        for i in range(self._capacity):
            if size == self._size:
                break

            chain: SingleLinkedList | None = self._entry_array[i]
            
            if chain is None:
                continue

            if not first_index:
                str_out += ", "
            else:
                first_index = False

            cur_node: SingleNode | None = chain.get_head() 

            # Iterate over chain and rehash each entry
            first_entry = True

            while cur_node is not None:

                if not first_entry:
                    str_out += ", "
                else:
                    first_entry = False

                cur_entry: Entry = cur_node.get_data()
                str_out += f"{str(cur_entry.get_key())}"
                size += 1
                cur_node = cur_node.get_next()

        str_out += "}"

        return str_out

