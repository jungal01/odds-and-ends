"""
This file originally was my experiment to test forms of caching through the
fibonacci sequence, but has become an experiment in benchmarking the
performance of different fibonacci algorithms. this experiment is not finished.


# testing environment:
    2c/4t intel celeron (laptop)
    4 Gib ddr3 memory
    Ubuntu 16.04
    kernel 4.17.10
    python 3.6.7
It has also become the grounds for testing python's limits when it comes to
large integers. For some unknown reason, a segmentation fault occurs when the
fibonacci number being calculated is around 20,145. faulthandler shows that
this occurs on the recursive portion of all of the O(n^2) functions, and it
appears to be inversely linked to memory in some way, seeing as memory usage is
almost directly linked to the fibonacci number able to be used. However, this
remains true regardless of how high the recursion limit is set to.

Some more debugging has proven to show that at 20000, the cached function
will segfault, while the memoized funcion works as expected. This remains true,
regardless of how large the lru_cache is set to.

In the terminal REPL, memoized fibonacci was able to be steadily stepped up to
260_000 at 5-10k intervals, proving definitively that this has nothing to do
with recursion at all, but it may be a stack overflow hitting a gaurd page.
This method managed to reach 97% usage on 4 Gib of memory, however, and hard
locked the computer before completing the calculation. The cached fib is far
more sensitive with the REPL, with a segfault occurring on any step above 10k.
I may be wrong, but this is starting to appear as if the actual problem has
something to do with how dictionaries and the cache are implemented.
Further experimentation is required before a bug report gets filed.
"""

from functools import lru_cache
from sys import setrecursionlimit as recurse
import time
import faulthandler
faulthandler.enable()

recurse(100_000_000)


def naive_fib(n):
    if n <= 2:
        return 1
    return naive_fib(n-1) + naive_fib(n - 2)


memo = {}
def memo_fib(n):
    val = 1
    if n in memo:
        return memo[n]
    if n <= 2:
        return val
    else:
        val = memo_fib(n - 1) + memo_fib(n - 2)
        memo[n] = val
        return val


@lru_cache(100_000_000)
def cached_fib(n):
    if n <= 2:
        return 1
    return cached_fib(n-1) + cached_fib(n - 2)


def bernat_fib(n):
    pass


def reddit_fib(n):
    pass


def main():
    start = time.time()
    for _ in range(5):
        memo_fib(15_000)
    end = time.time()

    print('memoized fibonacci: {}' .format(end-start))

    start = time.time()
    for _ in range(5):
        cached_fib(15_000)
    end = time.time()

    print('cached fibonacci: {}' .format(end-start))

    start = time.time()
    for _ in range(5):
        bernat_fib(15_000)
    end = time.time()

    print('bernat fibonacci: {}' .format(end-start))

    start = time.time()
    for _ in range(5):
        reddit_fib(15_000)
    end = time.time()

    print('redditors fibonacci: {}' .format(end-start))

    start = time.time()
    for _ in range(5):
        naive_fib(15_000)
    end = time.time()

    print('naive fibonacci: {}' .format(end-start))


if __name__ == "__main__":
    main()
