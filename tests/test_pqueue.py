from structures.m_pqueue import PriorityQueue
import random

# REF: ChatGPT generated code modified to fit data structure
# PROMPT: "Write unit tests for a priority queue ADT"
def test_empty_priority_queue() -> None:
    print("TESTING: test_empty_priority_queue()")
    pq = PriorityQueue()

    print(pq)

    assert(pq.is_empty() == True)
    assert(pq.get_size() == 0)

def test_insert_and_get_highest_priority() -> None:
    print("TESTING: test_insert_and_get_highest_priority()")
    pq = PriorityQueue()

    pq.insert(3, "Item1")
    pq.insert(1, "Item2")
    pq.insert(2, "Item3")

    assert(pq.is_empty() == False)
    assert(pq.get_size() == 3)

    print(pq)

    highest_priority_item = pq.get_min()
    assert(highest_priority_item == "Item2")
    assert(pq.get_size() == 3)

    print(pq)

def test_insert_and_remove_highest_priority() -> None:
    print("TESTING: test_insert_and_remove_highest_priority()")
    pq = PriorityQueue()

    pq.insert(3, "Item1")
    pq.insert(1, "Item2")
    pq.insert(2, "Item3")

    assert(pq.is_empty() == False)
    assert(pq.get_size() == 3)

    print(pq)

    highest_priority_item = pq.remove_min()
    assert(highest_priority_item == "Item2")
    assert(pq.get_size() == 2)

    print(pq)

def test_insert_and_get_multiple_times() -> None:
    print("TESTING: test_insert_and_get_multiple_times()")
    pq = PriorityQueue()

    pq.insert(3, "Item1")
    pq.insert(1, "Item2")
    pq.insert(2, "Item3")

    assert(pq.is_empty() == False)
    assert(pq.get_size() == 3)

    print(pq)

    highest_priority_item = pq.get_min()
    assert(highest_priority_item == "Item2")
    assert(pq.get_size() == 3)

    # Insert again after retrieval
    pq.insert(0, "Item4")
    assert(pq.get_size() == 4)

    print(pq)

    highest_priority_item = pq.get_min()
    assert(highest_priority_item == "Item4")
    assert(pq.get_size() == 4)

    print(pq)

def test_insert_same_priority() -> None:
    print("TESTING: test_insert_same_priority()")
    pq = PriorityQueue()

    pq.insert(3, "Item1")
    pq.insert(3, "Item2")
    pq.insert(3, "Item3")

    assert(pq.is_empty() == False)
    assert(pq.get_size() == 3)

    print(pq)

    highest_priority_item = pq.get_min()
    assert(highest_priority_item == "Item1")
    assert(pq.get_size() == 3)

    print(pq)

def test_insert_same_priority_and_remove_multiple_times() -> None:
    print("TESTING: test_insert_same_priority_and_remove_multiple_times()")
    pq = PriorityQueue()

    pq.insert(3, "Item1")
    pq.insert(3, "Item2")
    pq.insert(3, "Item3")

    assert(pq.is_empty() == False)
    assert(pq.get_size() == 3)

    print(pq)

    highest_priority_item = pq.remove_min()
    assert(highest_priority_item == "Item1")
    assert(pq.get_size() == 2)

    print(pq)

    highest_priority_item = pq.remove_min()
    assert(highest_priority_item == "Item2")
    assert(pq.get_size() == 1)

    print(pq)

    highest_priority_item = pq.remove_min()
    assert(highest_priority_item == "Item3")
    assert(pq.get_size() == 0)
    assert(pq.is_empty() == True)

    print(pq)

def test_insert_remove_multiple() -> None:
    print("TESTING: test_insert_remove_multiple()")
    pq = PriorityQueue()

    for i in range(100000):
        pq.insert_fifo(i)

    for i in range(100000):
        data = pq.remove_min()
        assert(data == i)