from structures.m_map import Map
from structures.m_entry import Entry

from typing import Any

class Set(Map):
    def add(self, key: Any) -> None:
        """
        """
        super().insert_kv(key, 0)