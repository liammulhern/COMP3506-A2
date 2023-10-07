import sys

def write_test_stub(test_name) -> str:
    str_out = f"""
def test_{test_name}() -> None:
    print("TESTING: test_{test_name}()")
    map = Map()"""
    return str_out

def write_test_calls(test_name) -> str:
    str_out = f"map_tests.test_{test_name}()"
    return str_out

if __name__ == "__main__":
    args = sys.argv[1:]
    for arg in args:
        # print(write_test_stub(arg))
        print(write_test_calls(arg))
