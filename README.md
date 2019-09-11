## Cython Examples
A few snippets and codes of Cython.

### 1. Installation
- Run `pip install -r requirements.txt`

### 2. Examples

#### `ex01_simple_comparison`
A simple comparison among *Pure Python* and some versions of *Cython* in terms of processing time for a very simple code that computes hypothetical taxes over incomes.

##### To run:
```
# First compile the Cython Modules
python setup.py build_ext --inplace  # on Linux
CC=gcc python setup.py build_ext --inplace  # on Mac

# Running the test script
python run_test.py
```

Since this example also tests the use of OpenMP to parallelize loops, the best thing to do on *Mac* is to use the **gcc** compiler instead of **clang** (default).

This example were adapted from the excellent talk [*"Easy wins with Cython: fast and multi-core by Caleb Hattingh"*](https://www.youtube.com/watch?v=NfnMJMkhDoQ) at PyCon Australia 2015.

Example only tested on Mac by using Python 3.6+ and gcc 7+.

Output of a given execution on my Mac:
```
1. Pure Python Function and Loop (function `sum`)
Time: 20.58034666 secs

2. Cython Function and Python Loop (function `sum`)
Time: 2.2217063470000014 secs

3. Cython Function and Loop
Time: 0.05373557400000095 secs

4. Cython Function and Parallelized Loop with OpenMP
Time: 0.043415286000001885 secs

5. Cython Function and Parallelized Loop with ThreadPoolExecutor
Time: 0.012918653999999918 secs
```
