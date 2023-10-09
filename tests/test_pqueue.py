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
    size: int = 0
    insertions: int = 0
    removals: int = 0

    random.seed = 123

    for i in range(100000):
        insert_or_remove = random.randint(0, 2)

        if insert_or_remove:
            priority = random.randint(0, 1000)
            data = random.randint(0, 1000)

            pq.insert(priority, data)
            insertions += 1

            size += 1
        else:
            data = pq.remove_min()
            removals += 1

            if size > 0:
                size -= 1

        assert(size == pq.get_size())

    print(f"After {i} iterations:\nInsertions: {insertions}\nRemovals: {removals}\nExpected size: {size}\nActual size: {pq.get_size()}")