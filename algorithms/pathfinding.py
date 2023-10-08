"""
COMP3506/7505 S2 2023
The University of Queensland

NOTE: This file will be used for marking.
"""

from structures.m_entry import Entry
from structures.m_single_linked_list import SingleLinkedList, SingleNode
from structures.m_extensible_list import ExtensibleList
from structures.m_graph import Graph, LatticeGraph, Node, LatticeNode
from structures.m_map import Map
from structures.m_set import Set
from structures.m_pqueue import PriorityQueue
from structures.m_stack import Stack
from structures.m_util import Hashable, TraversalFailure

from typing import Any

class TraversalNode:
    def __init__(self, id: int, path: ExtensibleList = ExtensibleList()) -> None:
        self._id = id
        self._path = path

        self.set_start(id)

    def __str__(self) -> str:
        return f"{self._id}:{self._path}"        

    def __repr__(self) -> str:
        return f"{self._id}:{self._path}"        

    def set_start(self, start_id: int) -> None:
        self._path.append(start_id)

    def get_id(self) -> int:
        return self._id

    def get_path(self) -> ExtensibleList:
        return self._path

def dfs_traversal(
    graph: Graph | LatticeGraph, origin: int, goal: int
) -> tuple[ExtensibleList, ExtensibleList] | tuple[TraversalFailure, ExtensibleList]:
    """
    Task 2.1: Depth First Search

    @param: graph
      The general graph or lattice graph to process
    @param: origin
      The ID of the node from which to start traversal
    @param: goal
      The ID of the target node

    @returns: tuple[ExtensibleList, ExtensibleList]
      1. The ordered path between the origin and the goal in node IDs;
      2. The IDs of all nodes in the order they were visited.
    @returns: tuple[TraversalFailure, ExtensibleList]
      1. TraversalFailure signals that the path between the origin and the target can not be found;
      2. The IDs of all nodes in the order they were visited.
    """
    # Stores the keys of the nodes in the order they were visited
    visited_order = ExtensibleList()

    stack: Stack = Stack()
    previous_nodes: Map = Map()
    visited_ids: Set = Set()

    stack.push(origin)

    while not stack.is_empty():
        current_node_id = stack.pop()

        if current_node_id == goal:
            visited_order.append(current_node_id)
            path = get_traversal_path(goal, previous_nodes)
            return (path, visited_order)

        # If a node has not been visited... visit it 
        if not visited_ids.exists(current_node_id):
            visited_order.append(current_node_id)
            visited_ids.add(current_node_id) 

        neighbour_nodes: list[Node] = graph.get_neighbours(current_node_id)
        neighbour_nodes_size: int = len(neighbour_nodes)

        for i in range(neighbour_nodes_size):
            neighbour_node_id: Node = neighbour_nodes[i].get_id()

            if not visited_ids.exists(neighbour_node_id):
                previous_nodes[neighbour_node_id] = current_node_id
                stack.push(neighbour_node_id)

    # If you couldn't get to the goal, you should return like this
    return (TraversalFailure.DISCONNECTED, visited_order)

def get_traversal_path(goal: int, previous_nodes: Map) -> ExtensibleList:
    current_id: int = goal 
    path = ExtensibleList()

    while current_id is not None:
        path.append(current_id)
        current_id = previous_nodes[current_id]

    path.reverse() 

    return path

def bfs_traversal(
    graph: Graph | LatticeGraph, origin: int, goal: int
) -> tuple[ExtensibleList, ExtensibleList] | tuple[TraversalFailure, ExtensibleList]:
    """
    Task 2.1: Breadth First Search

    @param: graph
      The general graph or lattice graph to process
    @param: origin
      The ID of the node from which to start traversal
    @param: goal
      The ID of the target node

    @returns: tuple[ExtensibleList, ExtensibleList]
      1. The ordered path between the origin and the goal in node IDs;
      2. The IDs of all nodes in the order they were visited.
    @returns: tuple[TraversalFailure, ExtensibleList]
      1. TraversalFailure signals that the path between the origin and the target can not be found;
      2. The IDs of all nodes in the order they were visited.
    """
    # Stores the keys of the nodes in the order they were visited
    visited_order = ExtensibleList()

    queue: PriorityQueue = PriorityQueue() 
    previous_nodes: Map = Map()
    visited_ids: Set = Set()

    queue.insert_fifo(origin)

    while not queue.is_empty():
        current_node_id: int = queue.remove_min()

        if current_node_id == goal:
            path = get_traversal_path(goal, previous_nodes)
            visited_order.append(current_node_id)
            return (path, visited_order)

        if not visited_ids.exists(current_node_id):
            visited_ids.add(current_node_id)
            visited_order.append(current_node_id)

            neighbour_nodes: list[Node] = graph.get_neighbours(current_node_id)
            neighbour_nodes_size: int = len(neighbour_nodes)

            for i in range(neighbour_nodes_size):
                neighbour_node_id: Node = neighbour_nodes[i].get_id()

                if not visited_ids.exists(neighbour_node_id):
                    previous_nodes[neighbour_node_id] = current_node_id
                    queue.insert_fifo(neighbour_node_id)

    # If you couldn't get to the goal, you should return like this
    return (TraversalFailure.DISCONNECTED, visited_order)

def greedy_traversal(
    graph: LatticeGraph, origin: int, goal: int
) -> tuple[ExtensibleList, ExtensibleList] | tuple[TraversalFailure, ExtensibleList]:
    """
    Task 2.2: Greedy Traversal

    @param: graph
      The lattice graph to process
    @param: origin
      The ID of the node from which to start traversal
    @param: goal
      The ID of the target node

    @returns: tuple[ExtensibleList, ExtensibleList]
      1. The ordered path between the origin and the goal in node IDs;
      2. The IDs of all nodes in the order they were visited.
    @returns: tuple[TraversalFailure, ExtensibleList]
      1. TraversalFailure signals that the path between the origin and the target can not be found;
      2. The IDs of all nodes in the order they were visited.
    """
    # Stores the keys of the nodes in the order they were visited
    visited_order = ExtensibleList()

    queue: PriorityQueue = PriorityQueue() 
    previous_nodes: Map = Map()
    visited_ids: Set = Set()

    queue.insert(0, origin)

    goal_node: LatticeNode = graph.get_node(goal)
    goal_position: tuple[int, int]= goal_node.get_coordinates()

    while not queue.is_empty():
        current_node_id: int = queue.remove_min()

        if current_node_id == goal:
            path = get_traversal_path(goal, previous_nodes)
            visited_order.append(current_node_id)
            return (path, visited_order)

        if not visited_ids.exists(current_node_id):
            visited_ids.add(current_node_id)
            visited_order.append(current_node_id)

            neighbour_nodes: list[Node] = graph.get_neighbours(current_node_id)
            neighbour_nodes_size: int = len(neighbour_nodes)

            for i in range(neighbour_nodes_size):
                neighbour_node_id: Node = neighbour_nodes[i].get_id()

                if not visited_ids.exists(neighbour_node_id):
                    previous_nodes[neighbour_node_id] = current_node_id
                    neighbour_node: LatticeNode = graph.get_node(neighbour_node_id)
                    neighbour_node_position: tuple[int, int] = neighbour_node.get_coordinates()

                    node_distance: float = get_node_distance(neighbour_node_position, goal_position)
                    queue.insert(node_distance, neighbour_node_id)

    # If you couldn't get to the goal, you should return like this
    return (TraversalFailure.DISCONNECTED, visited_order)

def get_node_distance(position_1: tuple[int, int], position_2: tuple[int, int]) -> float:
    x_1, y_1 = position_1
    x_2, y_2 = position_2

    return distance(x_1, y_1, x_2, y_2)

def distance(x_1: float, y_1: float, x_2: float, y_2: float) -> float:
    """
    Return the distance between a point at coordinate (x_1, y_1) and a point
    at coordinate (x_2, y_2). You may re-write this method with other
    parameters if you wish. Please comment on your choice of distance function.
    """
    # Calculate Manhattan Distance
    return abs(x_1 - x_2) + abs(y_1 - y_2)

def max_traversal(
    graph: LatticeGraph, origin: int, goal: int
) -> tuple[ExtensibleList, ExtensibleList] | tuple[TraversalFailure, ExtensibleList]:
    """
    Task 2.3: Maximize vertex visits traversal

    @param: graph
      The lattice graph to process
    @param: origin
      The ID of the node from which to start traversal
    @param: goal
      The ID of the target node

    @returns: tuple[ExtensibleList, ExtensibleList]
      1. The ordered path between the origin and the goal in node IDs;
      2. The IDs of all nodes in the order they were visited.
    @returns: tuple[TraversalFailure, ExtensibleList]
      1. TraversalFailure signals that the path between the origin and the target can not be found;
      2. The IDs of all nodes in the order they were visited.
    """
    visited_order = ExtensibleList()

    queue: PriorityQueue = PriorityQueue() 
    previous_nodes: Map = Map()
    visited_ids: Set = Set()

    queue.insert(0, origin)

    max_distance: int = get_node_distance(graph.get_dimensions(), (0, 0))

    goal_node: LatticeNode = graph.get_node(goal)
    goal_position: tuple[int, int]= goal_node.get_coordinates()

    while not queue.is_empty():
        current_node_id: int = queue.remove_min()

        if current_node_id == goal:
            path = get_traversal_path(goal, previous_nodes)
            visited_order.append(current_node_id)
            return (path, visited_order)

        if not visited_ids.exists(current_node_id):
            visited_ids.add(current_node_id)
            visited_order.append(current_node_id)

            neighbour_nodes: list[Node] = graph.get_neighbours(current_node_id)
            neighbour_nodes_size: int = len(neighbour_nodes)

            for i in range(neighbour_nodes_size):
                neighbour_node_id: Node = neighbour_nodes[i].get_id()

                if not visited_ids.exists(neighbour_node_id):
                    previous_nodes[neighbour_node_id] = current_node_id
                    neighbour_node: LatticeNode = graph.get_node(neighbour_node_id)
                    neighbour_node_position: tuple[int, int] = neighbour_node.get_coordinates()

                    node_distance: int = get_node_distance(neighbour_node_position, goal_position)
                    queue.insert(max_distance - node_distance, neighbour_node_id)

    # If you couldn't get to the goal, you should return like this
    return (TraversalFailure.DISCONNECTED, visited_order)


