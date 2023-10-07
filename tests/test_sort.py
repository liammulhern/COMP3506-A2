from structures.m_extensible_list import ExtensibleList

def test_empty_list() -> None:
    print("TESTING: test_empty_list()")
    e_list = ExtensibleList()

    print(e_list)

    e_list.sort()

    print(e_list)


def test_sorted_list() -> None:
    print("TESTING: test_sorted_list()")
    e_list = ExtensibleList()

    e_list.append(1)
    e_list.append(2)
    e_list.append(3)
    e_list.append(4)
    e_list.append(5)

    print(e_list)

    e_list.sort()

    print(e_list)


def test_reverse_sorted_list() -> None:
    print("TESTING: test_reverse_sorted_list()")
    e_list = ExtensibleList()

    e_list.append(5)
    e_list.append(4)
    e_list.append(3)
    e_list.append(2)
    e_list.append(1)

    print(e_list)

    e_list.sort()

    print(e_list)

def test_random_order_list() -> None:
    print("TESTING: test_random_order_list()")
    e_list = ExtensibleList()

    e_list.append(25)
    e_list.append(31)
    e_list.append(18)
    e_list.append(0)
    e_list.append(15)
    e_list.append(10)
    e_list.append(27)
    e_list.append(8)
    e_list.append(9)
    e_list.append(19)

    print(e_list)

    e_list.sort()

    print(e_list)

def test_duplicate_elements() -> None:
    print("TESTING: test_duplicate_elements()")
    e_list = ExtensibleList() 

    e_list.append(2)
    e_list.append(2)
    e_list.append(1)
    e_list.append(1)
    e_list.append(3)
    e_list.append(3)

    print(e_list)

    e_list.sort()

    print(e_list)

