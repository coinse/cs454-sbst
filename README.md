# CS454 Search Based Test Input Generation

The aim of this assignment is to implement search based test input generation technique for a subset of Python. To achieve this, you need to first instrument the target `.py` file, and then generate inputs for functions in the file in the format of pytest unit test cases, in such a way that they achieve the highest statement coverage possible.

To measure statement coverage, we will use `coverage.py`. 

```
$ pip install coverage
$ pip install pytest
$ coverage run -m pytest
$ coverage report
Name               Stmts   Miss  Cover   Missing
------------------------------------------------
example1.py            8      2    75%   7-9
test_example1.py       3      0   100%
------------------------------------------------
TOTAL                 11      2    82%
$
```

## Target Subset of Python

To complete the basic goal of this assignment, your test data generation technique should be able to achieve coverage against a Python program written using the following:

- local variables of type `int`
- `if` statements
- `for` and `while` loops
- comparison operators, `<`, `>`, `<=`, `>=`, `==`, and `!=`
- boolean predicates that use `and`, `or`, and `not`

