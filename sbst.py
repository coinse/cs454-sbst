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
    """

    test_file_content = '"""generate test file content here"""'
    test_file_name = os.path.join(os.path.dirname(args.target), "test_" + os.path.basename(args.target))
    with open(test_file_name, 'w') as f:
        f.write(test_file_content)

    print("Test suite generated in", test_file_name)


