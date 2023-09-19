# CS454 Search Based Test Input Generation

The aim of this assignment is to implement search based test input generation technique for a subset of Python. To achieve this, you need to first instrument the target `.py` file, and then generate inputs for functions in the file in the format of pytest unit test cases, in such a way that they achieve the highest statement coverage possible. To measure statement coverage, we will use [`coverage.py`](https://coverage.readthedocs.io/en/7.3.1/). 

## Target Subset of Python

To complete the basic goal of this assignment, your test data generation technique should be able to achieve coverage against a Python program written using the following:

- variables of type `int`
- `if` statements
- `for` and `while` loops
- comparison operators, `<`, `>`, `<=`, `>=`, `==`, and `!=`
- boolean predicates that use `and`, `or`, and `not`
- function calls within predicates

For the sake of simplicity, we will only target individual functions, so you only need to consider function arguments as inputs. All input variables will be of type `int`.

### Bonus Targets

Handling the following will give you additional points

- tertiary expressions in predicates, e.g., `if True if x == 42 else False:` or `if 4 if x > 0 else 2 > 3:`
- the `in` operators for collections, e.gl, `if x in y:` in which `y` is a set or a list
- implement Alternating Variable Method (AVM) as the solver

## Algorithms

Choose either one of Hill Climbing or Genetic Algorithm (GA). Name your tool as `sbst.py`. Your tool should accept a path to a Python file (`.py`) as input, and generate a unit test file that can be executed using PyTest, in the same directory as that of the target Python file. Consider the following example:

```
$ python sbst.py examples/example1.py
$ cd examples
$ pytest
```

If you want to check the coverage of your test cases, use `coverage.py`:

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
