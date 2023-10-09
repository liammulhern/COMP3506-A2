from structures.m_map import Map, LOAD_FACTOR_REHASH
from structures.m_entry import Entry

import random

def test_empty_map() -> None:
    print("TESTING: test_empty_map()")

    map = Map()

    print(map)

    assert(map.is_empty() == True)
    assert(map.get_size() == 0)   

def test_insert_not_empty() -> None:
    print("TESTING: test_insert_not_empty()")

    map = Map()

    e1 = Entry(1, "Item1")

    map.insert(e1)

    print(map)

    assert(map.is_empty() == False)
    assert(map.get_size() == 1)

def test_insert_size_increments() -> None:
    print("TESTING: test_insert_size_increments()")
    map = Map()

    e1 = Entry(1, "Item1")
    e2 = Entry(2, "Item2")
    e3 = Entry(3, "Item3")

    map.insert(e1)
    map.insert(e2)
    map.insert(e3)

    print(map)

    assert(map.is_empty() == False)
    assert(map.get_size() == 3)   

def test_insert_multiple_entry_types() -> None:
    print("TESTING: test_insert_multiple_entry_types()")
    map = Map()

    e1 = Entry(1, "Item1")
    e2 = Entry(2, "Item2")
    e3 = Entry(3, "Item3")
    e4 = Entry("ABC", "Item4")
    e5 = Entry("RANDOM_HASH", "Item5")

    map.insert(e1)
    map.insert(e2)
    map.insert(e3)
    map.insert(e4)
    map.insert(e5)

    print(map)

    assert(map.is_empty() == False)
    assert(map.get_size() == 5)   

def test_insert_same_key_replaces() -> None:
    print("TESTING: test_insert_same_key_replaces()")
    map = Map()

    e1 = Entry(1, "Item1")

    map.insert(e1)

    print(map)

    assert(map.is_empty() == False)
    assert(map.get_size() == 1)
    assert(map[1] == "Item1")

    e2 = Entry(1, "Item2")
    map.insert(e2)

    assert(map.is_empty() == False)
    assert(map.get_size() == 1)
    assert(map[1] == "Item2")

def test_insert_rehashes_on_capacity() -> None:
    print("TESTING: test_insert_rehashes_on_capacity()")
    map = Map()

    e1 = Entry(1, "Item1")
    e2 = Entry(2, "Item2")
    e3 = Entry(3, "Item3")
    e4 = Entry(4, "Item3")
    e5 = Entry(5, "Item3")
    e6 = Entry(6, "Item3")
    e7 = Entry(7, "Item3")
    e8 = Entry(8, "Item3")

    map.insert(e1)
    map.insert(e2)
    map.insert(e3)
    map.insert(e4)
    map.insert(e5)
    map.insert(e6)
    map.insert(e7)
    map.insert(e8)

    print(map)

    assert(map.is_empty() == False)
    assert(map.get_size() == 8)
    assert(map._get_load_factor() < LOAD_FACTOR_REHASH)

def test_find_returns_correct_value() -> None:
    print("TESTING: test_find_returns_correct_value()")
    map = Map()

    e1 = Entry(1, "Item1")
    e2 = Entry("A", "Item2")

    map.insert(e1)
    map.insert(e2)

    print(map)

    assert(map.is_empty() == False)
    assert(map.get_size() == 2)
    assert(map[1] == "Item1")
    assert(map.find(1) == "Item1")
    assert(map["A"] == "Item2")
    assert(map.find("A") == "Item2")

def test_find_no_key_returns_none() -> None:
    print("TESTING: test_find_no_key_returns_none()")
    map = Map()

    e1 = Entry(1, "Item1")
    e2 = Entry("A", "Item2")

    map.insert(e1)
    map.insert(e2)

    print(map)

    assert(map.is_empty() == False)
    assert(map.get_size() == 2)
    assert(map.find("B") == None)
 
def test_remove_no_key_no_changes() -> None:
    print("TESTING: test_remove_no_key_no_changes()")
    map = Map()

    e1 = Entry(1, "Item1")
    e2 = Entry("A", "Item2")

    map.insert(e1)
    map.insert(e2)

    print(map)

    assert(map.is_empty() == False)
    assert(map.get_size() == 2)

    map.remove("B")

    assert(map.is_empty() == False)
    assert(map.get_size() == 2)

    print(map)

def test_remove_key_removes_correct_key() -> None:
    print("TESTING: test_remove_key_removes_correct_key()")
    map = Map()

    e1 = Entry(1, "Item1")
    e2 = Entry("A", "Item2")

    map.insert(e1)
    map.insert(e2)

    print(map)

    assert(map.is_empty() == False)
    assert(map.get_size() == 2)

    map.remove(1)

    assert(map.is_empty() == False)
    assert(map.get_size() == 1)

    print(map)

def test_remove_key_removes_all_correct_key() -> None:
    print("TESTING: test_remove_key_removes_correct_key()")
    map = Map()

    e1 = Entry(1, "Item1")
    e2 = Entry("A", "Item2")

    map.insert(e1)
    map.insert(e2)

    print(map)

    assert(map.is_empty() == False)
    assert(map.get_size() == 2)

    map.remove(1)
    map.remove("A")
    map.remove("B")

    assert(map.is_empty() == True)
    assert(map.get_size() == 0)

    print(map)

def test_remove_key_decrements() -> None:
    print("TESTING: test_remove_key_decrements()")
    map = Map()

    e1 = Entry(1, "Item1")

    map.insert(e1)

    print(map)

    assert(map.is_empty() == False)
    assert(map.get_size() == 1)

    map.remove(1)

    assert(map.is_empty() == True)
    assert(map.get_size() == 0)

    print(map)

def test_insert_remove_multiple() -> None:
    print("TESTING: test_insert_remove_multiple()")
    map = Map()
    expected_map = {}
    size: int = 0
    insertions: int = 0
    removals: int = 0
    finds: int = 0

    random.seed(123)

    for i in range(1000000):
        map_type = random.randint(0, 5)

        key = i
        # key = random.randint(0, 10000)

        if i == 445:
            pass

        if map_type == 0:
            data = i

            if not map.exists(key):
                size += 1

            map[key] = data
            expected_map[key] = data

            insertions += 1
        elif map_type <= 2:
            data_1 = map[key]
            map.remove(key)
            data_2 = expected_map.pop(key, None)

            assert(data_1 == data_2)

            if data_1 is not None:
                removals += 1
                if size > 0:
                    size -= 1
        elif map_type == 1:
            assert(map.find(key) == expected_map.get(key, None))
            finds += 1

        assert(len(expected_map) == map.get_size())
        # assert(size == map.get_size())

    print(f"After {i} iterations:\nInsertions: {insertions}\nRemovals: {removals}\nFinds: {finds}\nExpected size: {size}\nActual size: {map.get_size()}")

