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
- the `in` operators for collections, e.g., `if x in y:` in which `y` is a set or a list
- handle the match-case syntax([spec](https://peps.python.org/pep-0634/) and [tutorial](https://peps.python.org/pep-0636/)), newly introduced in Python 3.10, for branch coverage

## Algorithms

First, implement hill climbing algorithm for the task. Name your tool as `sbst.py`. Your tool should accept a path to a Python file (`.py`) as input, and generate a unit test file that can be executed using PyTest, in the same directory as that of the target Python file. Consider the following example:

```
$ python sbst.py examples/example1.py
$ cd examples
$ pytest
```

The generated PyTest test code should be named as: `test_` + [target function name] + `.py`. For example, the output for a target file `foo.py` should be `test_foo.py`. The generated test functions should follow the following naming convention: `test_` + [target function name] + `_` + [index number]. For example, the 3rd PyTest test function for the target function named `bar` should be called: `test_bar_3`. 

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

## Bonus Goal

Implement one or more additional local search algorithms from below, and show that they are more efficient than hill climbing. Your report should clearly show that the additional algorithm outperforms the hill climbing algorithm you implemented.

- Simulated Annealing
- Alternating Variable Method
- Tabu Search

## Report

Write, and commit a simple report detailing your implementations, and include it as a PDF file in the repository. In particular, try to discuss the following point:

- What was your general approach towards instrumentation?
- How did you compute approach level?
- How many fitness evaluations does your algorithm require to achieve the reported coverage?
- Is there anything extra to the assignment that you have done? Bonus points, or even beyond those?