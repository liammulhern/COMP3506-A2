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
from random import randint 

from structures.m_entry import Entry
from structures.m_single_linked_list import SingleLinkedList
from structures.m_single_linked_list import SingleNode
from structures.m_doubly_linked_list import DoubleLinkedList
from structures.m_doubly_linked_list import DoubleNode
from structures.m_extensible_list import ExtensibleList

INITIAL_CAPACITY: int = 8
LOAD_FACTOR_REHASH: float = 2/3
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
        self._capacity: int = INITIAL_CAPACITY
        self._entry_array: list[DoubleLinkedList | None] = [None] * INITIAL_CAPACITY
        self._MAD_a: int = randint(1, PRIME_NUMBER - 1)
        self._MAD_b: int = randint(0, PRIME_NUMBER - 1)

    def __repr__(self) -> str:
        return str(self)

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

            chain: DoubleLinkedList | None = self._entry_array[i]
            
            if chain is None:
                continue

            if not first_index:
                str_out += ", "
            else:
                first_index = False

            cur_node: DoubleNode | None = chain.get_head() 

            # Iterate over chain and rehash each entry
            first_entry = True

            while cur_node is not None:

                if not first_entry:
                    str_out += ", "
                else:
                    first_entry = False

                cur_entry: Entry = cur_node.get_data()
                str_out += f"{str(cur_entry)}"
                size += 1
                cur_node = cur_node.get_next()

        str_out += "}"

        return str_out

    def insert(self, entry: Entry) -> Any | None:
        """
        Associate value v with key k for efficient lookups. You may wish
        to return the old value if k is already inside the map after updating
        to the new value v.
        """
        load_factor = self._get_load_factor()

        # Rehash map if load factor exceeds threshold (2/3)
        if load_factor > LOAD_FACTOR_REHASH:
            self._rehash()

        hash_index: int = self._get_hash_index_MAD(entry) 
        previous_value: Any | None = None 
        chain: DoubleLinkedList | None = self._entry_array[hash_index]
        entry_node: DoubleNode = DoubleNode(entry)

        # Initialise chain at hashed index if it does not currently have one
        if chain is None:
            chain = self._entry_array[hash_index] = DoubleLinkedList()
            chain.insert_to_back(entry_node)
            self._size += 1
            return previous_value

        # Iterate over chain until matching key is found or end is reached
        cur_node: DoubleNode | None = chain.find_element(entry)

        if cur_node is None:
            # Reached end of chain without finding matching key
            chain.insert_to_back(entry_node)
            self._size += 1
        else:
            # Found matching key in chain so update value
            cur_node.set_data(entry)

        return previous_value

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
        # You may or may not need this variable depending on your impl.
        dummy_entry = Entry(key, None) # Feel free to remove me...

        hash_index: int = self._get_hash_index_MAD(dummy_entry) 
        chain: DoubleLinkedList | None = self._entry_array[hash_index]

        # Initialise chain at hashed index if it does not currently have one
        if chain is None:
            return
        
        # Iterate over chain until matching key is found or end is reached
        removed_entry: Entry = chain.find_and_remove_element(dummy_entry)

        # Key was not in chain
        if removed_entry is None:
            return

        self._size -= 1

    def find(self, key: Any) -> Any | None:
        """
        Find and return the value v corresponding to key k if it
        exists; return None otherwise.
        """
        # You may or may not need this variable depending on your impl.
        dummy_entry: Entry = Entry(key, None) # Feel free to remove me...
        hash_index: int = self._get_hash_index_MAD(dummy_entry)
        chain: DoubleLinkedList | None = self._entry_array[hash_index]

        if chain is None:
            return None

        cur_node: DoubleNode | None = chain.find_element(dummy_entry)

        if cur_node is None:
            return None

        enrty: Entry = cur_node.get_data()

        return enrty.get_value()

    def exists(self, key: Any) -> bool:
        """
        Return true if a key exists in the map, false otherwise.
        """
        return self.find(key) is not None

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

    def get_keys(self) -> ExtensibleList:
        """
        Get all map keys as an extensible list 
        """ 
        size: int = 0
        keys: ExtensibleList = ExtensibleList() 


        for i in range(self._capacity):
            if size == self._size:
                break

            chain: SingleLinkedList | None = self._entry_array[i]
            
            if chain is None:
                continue

            cur_node: SingleNode | None = chain.get_head() 

            # Iterate over chain and rehash each entry
            while cur_node is not None:
                cur_entry: Entry = cur_node.get_data()
                keys.append(cur_entry.get_key())
                size += 1
                cur_node = cur_node.get_next()

        return keys

    def get_values(self) -> ExtensibleList:
        """
        Get all map values as an extensible list
        """
        size: int = 0
        values: ExtensibleList = ExtensibleList() 

        for i in range(self._capacity):
            if size == self._size:
                break

            chain: SingleLinkedList | None = self._entry_array[i]
            
            if chain is None:
                continue

            cur_node: SingleNode | None = chain.get_head() 

            # Iterate over chain and rehash each entry
            while cur_node is not None:
                cur_entry: Entry = cur_node.get_data()
                values.append(cur_entry.get_value())
                size += 1
                cur_node = cur_node.get_next()

        return values

    def get_items(self) -> ExtensibleList:
        size: int = 0
        items: ExtensibleList = ExtensibleList() 

        for i in range(self._capacity):
            if size == self._size:
                break

            chain: SingleLinkedList | None = self._entry_array[i]
            
            if chain is None:
                continue

            cur_node: SingleNode | None = chain.get_head() 

            while cur_node is not None:
                cur_entry: Entry = cur_node.get_data()
                items.append(cur_entry)
                size += 1
                cur_node = cur_node.get_next()

        return items

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

    def _rehash(self) -> None:
        """
        Resize and redistribute the keys of the map if the load factor exceeds 
        """
        old_capacity: int = self._capacity
        old_entry_array: list[DoubleLinkedList | None] = self._entry_array

        self._size = 0
        self._capacity *= 2
        self._entry_array = [None] * self._capacity
        actual_size: int = 0

        # Iterate over old entry array and rehash entries
        for i in range(old_capacity):
            chain: DoubleLinkedList | None = old_entry_array[i]

            if chain is None:
                continue
                
            cur_node: DoubleNode | None = chain.get_head() 
            actual_size += chain.get_size()

            # Iterate over chain and rehash each entry
            while cur_node is not None:
                cur_entry: Entry = cur_node.get_data()
                self.insert(cur_entry)
                cur_node = cur_node.get_next()

    def _get_load_factor(self) -> float:
        """
        Get the load factor of the map.
        """
        return self._size / self._capacity