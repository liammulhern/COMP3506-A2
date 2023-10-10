"""
COMP3506/7505 S2 2023
The University of Queensland

NOTE: This file will be used for marking.

Please read the following carefully. This file is used to implement a Map
class which supports efficient insertions, accesses, and deletions of
elements.

There is an Entry type defined in m_entry.py which *must* be used in your
map interface. The Entry is a very simple class that stores keys and values.
The special reason we make you use Entry types is because Entry extends the
Hashable class in m_util.py - by extending Hashable, you must implement
and use the `get_hash()` method inside Entry if you wish to use hashing to
implement your map. We *will* be assuming Entry types are used in your Map
implementation. Sorry for any inconvenience this causes (hopefully none!).
Note that if you opt to not use hashing, then you can simply override the
get_hash function to return -1 for example.
"""

from typing import Any
import time
from random import randint 

from structures.m_entry import Entry
from structures.m_extensible_list import ExtensibleList

INITIAL_CAPACITY: int = 8
LOAD_FACTOR_REHASH: float = 0.6
PRIME_NUMBER: int = 109345121

class Map:
    """
    An implementation of the Map ADT.
    The provided methods consume keys and values via the Entry type.
    """
    def __init__(self) -> None:
        """
        Construct the map.
        You are free to make any changes you find suitable in this function
        to initialise your map.
        """
        self._size: int = 0
        self._apparent_size: int = 0
        self._capacity: int = INITIAL_CAPACITY
        self._entry_array: list[Any | None] = [None] * INITIAL_CAPACITY
        self._MAD_a: int = randint(1, PRIME_NUMBER - 1)
        self._MAD_b: int = randint(0, PRIME_NUMBER - 1)

    def __repr__(self) -> str:
        return str(self)

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

            str_out += str(entry)
            size += 1

        str_out += "}"

        return str_out

    def insert(self, entry: Entry) -> Any | None:
        """
        Associate value v with key k for efficient lookups. You may wish
        to return the old value if k is already inside the map after updating
        to the new value v.
        """
        load_factor = self._get_load_factor()

        # Rehash map if load factor exceeds threshold
        if load_factor > LOAD_FACTOR_REHASH:
            self._rehash()

        initial_hash_index: int = self._get_hash_index(entry) 
        hash_index = initial_hash_index

        probe_iteration: int = 0
        update: bool = False

        while self._entry_array[hash_index] is not None:
            cur_entry: Entry = self._entry_array[hash_index]
           
            if cur_entry == entry:
                update = True
                break
 
            hash_index = self._get_probe_index(initial_hash_index, probe_iteration)
            probe_iteration += 1

        self._entry_array[hash_index] = entry

        if not update:
            self._size += 1
            self._apparent_size += 1

    def insert_kv(self, key: Any, value: Any) -> Any | None:
        """
        A version of insert which wraps a given key/value in an Entry type.
        Handy if you wish to provide keys and values directly to the insert
        function. It will return the value returned by insert, so keep this
        in mind.
        """
        entry = Entry(key, value)
        return self.insert(entry)
      
    def __setitem__(self, key: Any, value: Any) -> None:
        """
        For convenience, you may wish to use this as an alternative
        for insert as well. However, this version does _not_ return
        anything. Can be used like: my_map[some_key] = some_value
        """
        entry = Entry(key, value)
        self.insert(entry)

    def remove(self, key: Any) -> None:
        """
        Remove the key/value pair corresponding to key k from the
        data structure. Don't return anything.
        """
        dummy_entry = Entry(key, None)
        
        initial_hash_index: int = self._get_hash_index(dummy_entry) 
        hash_index = initial_hash_index

        probe_iteration: int = 0
        
        while self._entry_array[hash_index] is not None:
            entry: Entry = self._entry_array[hash_index]

            if entry == dummy_entry:
                self._entry_array[hash_index] = Entry(None, None)
                self._size -= 1
                return 

            hash_index = self._get_probe_index(initial_hash_index, probe_iteration)
            probe_iteration += 1

    def find(self, key: Any) -> Any | None:
        """
        Find and return the value v corresponding to key k if it
        exists; return None otherwise.
        """
        dummy_entry = Entry(key, None)
        
        initial_hash_index: int = self._get_hash_index(dummy_entry) 
        hash_index = initial_hash_index

        probe_iteration: int = 0

        while self._entry_array[hash_index] is not None:
            entry: Entry = self._entry_array[hash_index]

            if entry == dummy_entry:
                return entry.get_value()

            hash_index = self._get_probe_index(initial_hash_index, probe_iteration)
            probe_iteration += 1

        return None

    def exists(self, key: Any) -> bool:
        """
        Return true if a key exists in the map, false otherwise.
        """
        return self.find(key) is not None

    def get_keys(self) -> ExtensibleList:
        current_size: int = 0
        keys: ExtensibleList = ExtensibleList()
        empty_entry: Entry = Entry(None, None)

        for i in range(self._capacity):
            if current_size == self._size:
                break

            entry: Entry | None = self._entry_array[i]

            if entry is None or entry == empty_entry:
                continue

            keys.append(entry.get_key())
            current_size += 1
        
        return keys

    def get_values(self) -> ExtensibleList:
        current_size: int = 0
        values: ExtensibleList = ExtensibleList()
        empty_entry: Entry = Entry(None, None)

        for i in range(self._capacity):
            if current_size == self._size:
                break

            entry: Entry | None = self._entry_array[i]

            if entry is None or entry == empty_entry:
                continue

            values.append(entry.get_value())
            current_size += 1
        
        return values

    def get_items(self) -> ExtensibleList:
        current_size: int = 0
        items: ExtensibleList = ExtensibleList()
        empty_entry: Entry = Entry(None, None)

        for i in range(self._capacity):
            if current_size == self._size:
                break

            entry: Entry | None = self._entry_array[i]

            if entry is None or entry == empty_entry:
                continue

            items.append(entry)
            current_size += 1
        
        return items

    def __getitem__(self, key: Any) -> Any | None:
        """
        For convenience, you may wish to use this as an alternative
        for find()
        """
        return self.find(key) 

    def get_size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def _get_hash_index(self, entry: Entry) -> int:
        """
        Get the hash index of the entry by taking mod N
        """
        hash_index: int = entry.get_hash() % self._capacity

        return hash_index

    def _get_hash_index_MAD(self, entry: Entry) -> int:
        """
        Implements MAD compression:
            h(y) = ((ay + b) mod p ) mod N
        """
        hash_index: int = ((self._MAD_a * entry.get_hash() + self._MAD_b) % PRIME_NUMBER) % self._capacity

        return hash_index

    def _get_probe_index(self, hash_index: int, iteration: int) -> int:
        return (hash_index + iteration) % self._capacity

    def _get_quadratic_probe_index(self, hash_index: int, iteration: int) -> int:
        """
        Get quadratic probe index
        """
        return (hash_index + pow(iteration, 2)) % self._capacity

    def _get_load_factor(self) -> float:
        """
        Get the load factor of the map.
        """
        return self._apparent_size / self._capacity

    def _rehash(self) -> None:
        """
        Rehash the map and increase its capacity
        """
        old_capacity: int = self._capacity
        old_size: int = self._size
        old_entry_array: list[Entry | None] = self._entry_array
        
        self._size = 0
        self._apparent_size = 0
        self._capacity *= 3
        self._entry_array = [None] * self._capacity
        
        current_size: int = 0

        empty_entry: Entry = Entry(None, None)

        for i in range(old_capacity):
            if current_size == old_size:
                break

            entry: Entry | None = old_entry_array[i]

            if entry is None or entry == empty_entry:
                continue

            self.insert(entry)
            current_size += 1