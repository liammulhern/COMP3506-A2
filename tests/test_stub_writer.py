import sys
import random 

def write_test_stub(test_name) -> str:
    str_out = f"""
def test_{test_name}() -> None:
    print("TESTING: test_{test_name}()")
    e_list = ExtensibleList()"""
    return str_out

def write_test_calls(test_name) -> str:
    str_out = f"sort_tests.test_{test_name}()"
    return str_out

def write_random_list_init() -> str:
    random_int = random.randint(0, 50)
    str_out = f"e_list.append({random_int})"

    return str_out

def write_tests() -> None:
    args = sys.argv[1:]
    for arg in args:
        # print(write_test_stub(arg))
        print(write_test_calls(arg))

def generate_large_connected_graph(num_nodes):
    graph = {}
    
    # Create nodes with random connections
    for i in range(1, num_nodes + 1):
        vertices = random.sample(range(1, num_nodes + 1), random.randint(1, min(10, num_nodes - 1)))
        graph[i] = vertices
    
    return graph

# Generate a large connected graph with 100 nodes
num_nodes = 30
large_graph = generate_large_connected_graph(num_nodes)

# Print the graph in the specified format
for node, vertices in large_graph.items():
    print(f"{node}: {' '.join(map(str, vertices))}")


def write_random_list() -> None:
    for i in range(10):
        print(write_random_list_init())

if __name__ == "__main__":
    write_tests()
    # write_random_list()