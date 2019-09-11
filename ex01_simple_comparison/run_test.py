from concurrent.futures import ThreadPoolExecutor
import random
import timeit

import numpy as np
from _tax import tax_cython, tottax, tottax_openmp  # cython module


# pure python
def tax_python(amount):
    if amount <= 18200:
        return 0
    elif amount <= 37000:
        return 0.19 * (amount - 18200)
    elif amount <= 8000:
        return 3572 + 0.325 * (amount - 3700)
    elif amount <= 180000:
        return 17547 + 0.37 * (amount - 8000)
    else:
        return 54547 + 0.45 * (amount - 180000)



if __name__ == "__main__":
    incomes = np.random.uniform(5000, 500000 + 1, 10000000)

    print("1. Pure Python Function and Loop (function `sum`)")
    start = timeit.default_timer()
    sum(tax_python(i) for i in incomes)
    stop = timeit.default_timer()
    print(f'Time: {stop - start} secs\n')

    print("2. Cython Function and Python Loop (function `sum`)")
    start = timeit.default_timer()
    sum(tax_cython(i) for i in incomes)
    stop = timeit.default_timer()
    print(f'Time: {stop - start} secs\n')

    print("3. Cython Function and Loop")
    start = timeit.default_timer()
    tottax(incomes)
    stop = timeit.default_timer()
    print(f'Time: {stop - start} secs\n')

    print("4. Cython Function and Parallelized Loop with OpenMP (`prange`)")
    start = timeit.default_timer()
    tottax_openmp(incomes)
    stop = timeit.default_timer()
    print(f'Time: {stop - start} secs\n')

    print("5. Cython Function and Parallelized Loop with ThreadPoolExecutor")
    start = timeit.default_timer()
    with ThreadPoolExecutor(max_workers=8) as exe:
        sections = np.array_split(incomes, 8)
        jobs = [exe.submit(tottax, s) for s in sections]
    sum(job.result() for job in jobs)
    stop = timeit.default_timer()
    print(f'Time: {stop - start} secs\n')
