"""
This file originally was my experiment to test forms of caching through the
fibonacci sequence, but has become an experiment in benchmarking the performance
of different fibonacci algorithms. this experiment is not finished yet.
"""

from functools import lru_cache
from sys import setrecursionlimit as recurse
import datetime

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


@lru_cache(100000)
def cached_fib(n):
    if n <= 2:
        return 1
    return cached_fib(n-1) + cached_fib(n - 2)


def bernat_fib(n):
    pass


def reddit_fib(n):
    pass


def main():
    start = datetime.time()
    for _ in range(5):
        memo_fib(25_000)
    end = datetime.time()

    print('memoized fibonacci: {}' .format(end-start))

    start = datetime.time()
    for _ in range(5):
        cached_fib(25_000)
    end = datetime.time()

    print('cached fibonacci: {}' .format(end-start))

    start = datetime.time()
    for _ in range(5):
        bernat_fib(25_000)
    end = datetime.time()

    print('bernat fibonacci: {}' .format(end-start))

    start = datetime.time()
    for _ in range(5):
        reddit_fib(25_000)
    end = datetime.time()

    print('redditors fibonacci: {}' .format(end-start))

    start = datetime.time()
    for _ in range(5):
        naive_fib(25_000)
    end = datetime.time()

    print('naive fibonacci: {}' .format(end-start))


if __name__ == "__main__":
    main()
