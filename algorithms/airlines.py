"""
COMP3506/7505 S2 2023
The University of Queensland

NOTE: This file will be used for marking.
"""

from structures.m_entry import Destination
from structures.m_extensible_list import ExtensibleList
from structures.m_graph import Graph, Node
from structures.m_map import Map
from structures.m_set import Set
from structures.m_pqueue import PriorityQueue
from structures.m_stack import Stack
from structures.m_single_linked_list import SingleLinkedList
from structures.m_util import TraversalFailure
import math


def has_cycles(graph: Graph) -> bool:
    """
    Task 3.1: Cycle detection

    @param: graph
      The general graph to process

    @returns: bool
      Whether or not the graph contains cycles
    """
    stack: Stack = Stack()
    visited_ids: Set = Set()
    previous_node: Map = Map()

    # Iterate over all nodes in the graph
    for i in range(graph.get_size()):
        origin_node: Node = graph.get_node(i)
        origin_node_id: int = origin_node.get_id()

        if not visited_ids.exists(origin_node_id):
            stack.push(origin_node_id)
            previous_node[origin_node_id] = None

            # Complete DFS for iterated origin node
            while not stack.is_empty():
                current_node_id = stack.pop()
                visited_ids.add(current_node_id)

                neighbour_nodes: list[Node] = graph.get_neighbours(current_node_id)
                neighbour_nodes_size: int = len(neighbour_nodes)

                for j in range(neighbour_nodes_size):
                    neighbour_node_id: Node = neighbour_nodes[j].get_id()

                    if not visited_ids.exists(neighbour_node_id):
                        previous_node[neighbour_node_id] = current_node_id
                        stack.push(neighbour_node_id)
                    elif previous_node[current_node_id] != neighbour_node_id:
                        # If the neighbour node has neen visited and
                        # the previously visited node of the current node is not a
                        # neighbour then a cycle has been found
                        return True


def enumerate_hubs(graph: Graph, min_degree: int) -> ExtensibleList:
    """
    Task 3.2: Hub enumeration

    @param: graph
      The general graph to process
    @param: min_degree
      the lowest degree a vertex can have to be considered a hub

    @returns: ExtensibleList
      A list of all Node IDs corresponding to the largest subgraph
      where each vertex has a degree of at least min_degree.
    """
    largest_subgraph: ExtensibleList = _find_subgraphs_of_degree(graph, min_degree)

    largest_subgraph.sort()

    return largest_subgraph


def _find_subgraphs_of_degree(graph: Graph, min_degree: int) -> SingleLinkedList:
    """
    Process:
        1. Find degree of all nodes in graph.
        2. If a node has degree less than the minimum, remove it from the graph.
        3. Recalculate neighbour degrees of removed node, if they are now below
        the minimum degree remove them from graph.
        4. Repeat 3.
    """
    stack: Stack = Stack()
    visited_ids: Set = Set()
    visited_order: ExtensibleList = ExtensibleList()

    # Iterate over all nodes in the graph
    for i in range(graph.get_size()):
        if visited_ids.get_size() == graph.get_size():
            break

        origin_node: Node = graph.get_node(i)
        origin_node_id: int = origin_node.get_id()

        if not visited_ids.exists(origin_node_id):
            stack.push(origin_node_id)

            # Complete DFS for iterated origin node
            while not stack.is_empty():
                current_node_id = stack.pop()

                neighbour_nodes: list[Node] = graph.get_neighbours(current_node_id)
                neighbour_nodes_size: int = len(neighbour_nodes)

                # If a node has not been visited... visit it
                if not visited_ids.exists(current_node_id):
                    visited_ids.add(current_node_id)

                    if neighbour_nodes_size < min_degree:
                        graph.remove_node(current_node_id)
                        _update_neighbour_node_degree(graph, neighbour_nodes, visited_order, min_degree)
                        continue
                    else:
                        visited_order.append(current_node_id)
                else:
                    continue

                for j in range(neighbour_nodes_size):
                    neighbour_node_id: Node = neighbour_nodes[j].get_id()

                    if not visited_ids.exists(neighbour_node_id):
                        stack.push(neighbour_node_id)

    return visited_order


def _update_neighbour_node_degree(graph: Graph, neighbour_nodes: list[Node],
                                  visited_order: ExtensibleList, min_degree: int) -> None:
    """
    """
    neighbour_nodes_size: int = len(neighbour_nodes)

    for i in range(neighbour_nodes_size):
        current_node_id: Node = neighbour_nodes[i].get_id()
        current_neighbour_nodes: list[Node] = graph.get_neighbours(current_node_id)
        current_neighbour_nodes_size: int = len(current_neighbour_nodes)

        if current_neighbour_nodes_size == 0:
            continue

        if current_neighbour_nodes_size < min_degree:
            graph.remove_node(current_node_id)
            visited_order.remove(current_node_id)
            _update_neighbour_node_degree(graph, current_neighbour_nodes, visited_order, min_degree)


def calculate_flight_budget(graph: Graph, origin: int, stopover_budget: int, monetary_budget: int) -> ExtensibleList:
    """
    Task 3.3: Big Bogan Budget Bonanza

    @param: graph
      The general graph to process
    @param: origin
      The origin from where the passenger wishes to fly
    @param: stopover_budget
      The maximum number of stopovers the passenger is willing to make
    @param: monetary_budget
      The maximum amount of money the passenger is willing to spend

    @returns: ExtensibleList
      The sorted list of viable destinations satisfying stopover and budget constraints.
      Each element of the ExtensibleList should be of type Destination - see
      m_entry.py for the definition of that type.
    """
    budget_costs: Map = Map()
    stopover_costs: Map = Map()
    visited_ids: Set = Set()

    budget_costs.insert(Destination(origin, None, 0, 0))
    stopover_costs[origin] = -1

    queue: PriorityQueue = PriorityQueue()
    queue.insert(0, origin)

    while not queue.is_empty():
        monetary_cost, current_node_id = queue.remove_min_node()

        if visited_ids.exists(current_node_id):
            continue

        visited_ids.add(current_node_id)

        neighbour_nodes: list[Node] = graph.get_neighbours(current_node_id)
        neighbour_nodes_size: int = len(neighbour_nodes)

        for i in range(neighbour_nodes_size):
            neighbour_node, neighbour_node_cost = neighbour_nodes[i]
            neighbour_node_id = neighbour_node.get_id()

            new_monetary_cost: int = monetary_cost + neighbour_node_cost
            old_budget_cost_node: int | None = budget_costs[neighbour_node_id]

            if old_budget_cost_node is None or new_monetary_cost < old_budget_cost_node:

                new_stopover_cost = stopover_costs[current_node_id] + 1
                stopover_costs[neighbour_node_id] = new_stopover_cost

                if new_monetary_cost <= monetary_budget and new_stopover_cost <= stopover_budget:
                    budget_costs.insert(Destination(neighbour_node_id, None, new_monetary_cost, new_stopover_cost))

                queue.insert(new_monetary_cost, neighbour_node_id)

    budget_costs.remove(origin)
    budget_costs_sorted = budget_costs.get_items()
    budget_costs_sorted.sort()

    return budget_costs_sorted


def maintenance_optimisation(graph: Graph, origin: int) -> ExtensibleList:
    """
    Task 3.4: BA Field Maintenance Optimisation

    @param: graph
      The general graph to process
    @param: origin
      The origin where the aircraft requiring maintenance is

    @returns: ExtensibleList
      The list of all reachable destinations with the shortest path costs.
      Please use the Entry type here, with the key being the node identifier,
      and the value being the cost.
    """
    budget_costs: Map = Map()
    visited_ids: Set = Set()

    budget_costs[origin] = 0

    queue: PriorityQueue = PriorityQueue()
    queue.insert(0, origin)

    while not queue.is_empty():
        monetary_cost, current_node_id = queue.remove_min_node()

        if visited_ids.exists(current_node_id):
            continue

        visited_ids.add(current_node_id)

        neighbour_nodes: list[Node] = graph.get_neighbours(current_node_id)
        neighbour_nodes_size: int = len(neighbour_nodes)

        for i in range(neighbour_nodes_size):
            neighbour_node, neighbour_node_cost = neighbour_nodes[i]
            neighbour_node_id = neighbour_node.get_id()

            new_monetary_cost: int = monetary_cost + neighbour_node_cost
            old_budget_cost: int | None = budget_costs[neighbour_node_id]

            if old_budget_cost is None or new_monetary_cost < budget_costs[neighbour_node_id]:
                budget_costs[neighbour_node_id] = new_monetary_cost

                queue.insert(new_monetary_cost, neighbour_node_id)

    budget_costs.remove(origin)
    budget_costs_sorted = budget_costs.get_items()
    budget_costs_sorted.sort()

    return budget_costs_sorted


def all_city_logistics(graph: Graph) -> Map:
    """
    Task 3.5: All City Logistics

    @param: graph
      The general graph to process

    @returns: Map
      The map containing node pairs as keys and the cost of the shortest path
      between them as values. So, the node pairs should be inserted as keys
      of the form "0_1" where 0 is the origin node and 1 is the target node
      (their type is a string using an underscore as a seperator). The
      value should be an integer (cost of the path), or a TraversalFailure
      enumeration.
    """
    node_pair_costs: Map = _create_graph_cartesian_product_map(graph)

    for origin in range(graph.get_size()):
        _find_graph_costs_and_negative_cycles(graph, node_pair_costs, origin)

    # Remove any self referencing entries
    for origin in range(graph.get_size()):
        node_pair_same: str = f"{origin}_{origin}"
        node_pair_costs.remove(node_pair_same)

    return node_pair_costs


def _create_graph_cartesian_product_map(graph: Graph) -> Map:
    """
    Creates a map with keys as the cartesian product of graph nodes.
    """
    node_cartesian_product: Map = Map()

    # Create cartesian pairs for integers 0 to n
    for i in range(graph.get_size()):
        for j in range(i, graph.get_size()):
            product_1: str = f"{i}_{j}"
            product_2: str = f"{j}_{i}"
            node_cartesian_product[product_1] = TraversalFailure.DISCONNECTED
            node_cartesian_product[product_2] = TraversalFailure.DISCONNECTED

    return node_cartesian_product


def _find_graph_costs_and_negative_cycles(graph: Graph, node_pairs_costs: Map, origin: int) -> Set:
    """
    Use the Bellman-Ford algorithm to find negative cycles in the graph and
    return a set of visited nodes.
    """
    neighbours = graph.get_neighbours(origin)

    if len(neighbours) == 0:
        return

    edges = graph.get_edges()
    origin_node_pair: str = f"{origin}_{origin}"
    node_pairs_costs[origin_node_pair] = 0

    # Perform Bellman-Ford algorithm to find the cost of reaching each avaliable node.
    for i in range(graph.get_size() - 1):
        _bellman_ford_algorithm(edges, node_pairs_costs, origin, negative_cycle=False)

    # Repeat Bellman-Ford algorithm again to see if any costs change,
    # if they do it is a negative cycle.
    for i in range(graph.get_size() - 1):
        _bellman_ford_algorithm(edges, node_pairs_costs, origin, negative_cycle=True)


def _bellman_ford_algorithm(
        edges: list[list[tuple[int, int]]] | None,
        node_pairs_costs: Map,
        origin: int,
        negative_cycle: bool = False) -> None:
    """
    Implementation of the Bellman-Ford algorithm, to find negative cycles and minimum cost.
    """
    for node_from_id in range(len(edges)):
        for k in range(len(edges[node_from_id])):
            edge = edges[node_from_id][k]
            node_to_id, node_cost = edge

            # Create the key from the origin to the edges
            node_pair_from: str = f"{origin}_{node_from_id}"
            node_pair_to: str = f"{origin}_{node_to_id}"

            node_pair_cost_from = node_pairs_costs[node_pair_from]

            # Update node 1 cost if path is disconnected or negative cycle
            if node_pair_cost_from is TraversalFailure.DISCONNECTED:
                continue
            elif node_pair_cost_from is TraversalFailure.NEGATIVE_CYCLE:
                node_pair_cost_from = -math.inf

            node_pair_cost_to = node_pairs_costs[node_pair_to]

            # Update node 2 cost if path is disconnected or negative cycle
            if node_pair_cost_to is TraversalFailure.DISCONNECTED:
                node_pair_cost_to = math.inf
            elif node_pair_cost_to is TraversalFailure.NEGATIVE_CYCLE:
                continue

            # Check if new shortest path is found
            if node_pair_cost_from + node_cost < node_pair_cost_to:
                if negative_cycle:
                    node_pairs_costs[node_pair_to] = TraversalFailure.NEGATIVE_CYCLE
                else:
                    node_pairs_costs[node_pair_to] = node_pair_cost_from + node_cost
