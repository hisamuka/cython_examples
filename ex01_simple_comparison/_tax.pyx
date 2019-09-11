from cython.parallel import prange, threadid

cpdef double tax_cython(double amount) nogil:
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


cpdef double tottax(double[:] incomes):
    cdef int i = 0
    cdef int n = incomes.shape[0]
    cdef double tot = 0.0

    with nogil:
        for i in range(n):
            tot += tax_cython(incomes[i])

    return tot


cpdef double tottax_openmp(double[:] incomes):
    cdef int i = 0
    cdef int n = incomes.shape[0]
    cdef double tot = 0.0

    for i in prange(n, num_threads=8, nogil=True):
        tot += tax_cython(incomes[i])

    return tot
