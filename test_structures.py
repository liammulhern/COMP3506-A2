"""
COMP3506/7505 S2 2023
The University of Queensland

NOTE: This file will not be used for marking and is here to provide you with
a simple way of testing your data structures. You may edit this file by adding
your own test functionality.
"""

# Import helper libraries
import sys
import argparse
import time
import random

# Import our data structures from A1 (just in case you want them)
from structures.m_extensible_list import ExtensibleList
from structures.m_stack import Stack
from structures.m_single_linked_list import SingleNode, SingleLinkedList

# Import our new structures
from structures.m_entry import *
from structures.m_pqueue import PriorityQueue
from structures.m_map import Map

import tests.test_pqueue as pqueue_tests
import tests.test_map as map_tests

def test_pqueue() -> None:
    """
    A simple set of tests for the priority queue.
    This is not marked and is just here for you to test your code.
    """
    print ("==== Executing Priority Queue Tests ====")

    pqueue_tests.test_empty_priority_queue()
    pqueue_tests.test_insert_and_remove_highest_priority()
    pqueue_tests.test_insert_and_get_highest_priority()
    pqueue_tests.test_insert_and_get_multiple_times()
    pqueue_tests.test_insert_same_priority()
    pqueue_tests.test_insert_same_priority_and_remove_multiple_times()

def test_map() -> None:
    """
    A simple set of tests for the associative map.
    This is not marked and is just here for you to test your code.
    """
    print ("==== Executing Map Tests ====")

    map_tests.test_empty_map()
    map_tests.test_insert_size_increments()
    map_tests.test_insert_multiple_entry_types()
    map_tests.test_insert_same_key_replaces()
    map_tests.test_insert_rehashes_on_capacity()
    map_tests.test_find_returns_correct_value()
    map_tests.test_find_no_key_returns_none()
    map_tests.test_remove_no_key_no_changes()
    map_tests.test_remove_key_removes_correct_key()
    map_tests.test_remove_key_removes_all_correct_key()
    map_tests.test_remove_key_decrements()

def test_sort() -> None:
    """
    A simple set of tests for your sorting algorithm.
    This si not marked and is just here for you to test your code.
    """
    print ("==== Executing Sorting Tests ====")
    my_list = ExtensibleList()
    my_list.append(3)
    my_list.append(8)
    my_list.append(1)
    my_list.append(4)
    my_list.append(7)
    print("Before = ", my_list)
    my_list.sort()
    print("After = ", my_list)
    ###
    # DO RIGOROUS TESTING HERE!
    ###

def test_debug():
    test_map()
    sys.exit()

# The actual program we're running here
if __name__ == "__main__":
    # Get and parse the command line arguments
    parser = argparse.ArgumentParser(description='COMP3506/7505 Assignment Two: Data Structure Tests')

    parser.add_argument('--pq', action='store_true', help="Run priority queue tests?")
    parser.add_argument('--map',     action='store_true', help="Run map tests?")
    parser.add_argument('--sort',     action='store_true', help="Run sort tests?")
    parser.set_defaults(pq=False, map=False)

    args = parser.parse_args()
    
    # No arguments passed
    if len(sys.argv) == 1:
        parser.print_help() 
        test_debug()
        sys.exit(-1)

    # Test each 
    if args.pq:
        test_pqueue()
    if args.map:
        test_map()
    if args.sort:
        test_sort()
