import argparse
import ast
import os

# usage: python sbst.py examples/example$N$.py
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("target", help="the target python file to generate unit tests for")
    args = parser.parse_args()

    with open(args.target, "r") as f:
        code = f.read()
    
    tree = ast.parse(code)
    print(ast.dump(tree))

    """
    TODO: generate a test suite for the target python file
    You can modify the code below to generate a test suite for any target python file in the examples folder.
    """

    target_module = os.path.basename(args.target).removesuffix(".py")

    test_file_content = f'''
import {target_module}
def test_sample():
    {target_module}.foo(1, 1)
    '''.strip()
    test_file_name = os.path.join(os.path.dirname(args.target), "test_" + os.path.basename(args.target))
    with open(test_file_name, 'w') as f:
        f.write(test_file_content)

    print("Test suite generated in", test_file_name)


