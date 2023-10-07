import sys
from random import randint

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
    random_int = randint(0, 50)
    str_out = f"e_list.append({random_int})"

    return str_out

def write_tests() -> None:
    args = sys.argv[1:]
    for arg in args:
        # print(write_test_stub(arg))
        print(write_test_calls(arg))

def write_random_list() -> None:
    for i in range(10):
        print(write_random_list_init())

if __name__ == "__main__":
    write_tests()
    # write_random_list()