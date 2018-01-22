"""
This file was my experiment to test forms of caching through the fibonacci sequence. The decorator is from the built in module functools.
The dictionary is a form of caching as well, known as memoization. I was attempting to directly compare the two forms by manually timing each 
method. As far as I could tell, they both perform at the same speed.
"""

from functools import lru_cache

#memo = {}

@lru_cache(100000) # decorator


def fib(n):
    value = 1

 #   if n in memo:
 #       value = memo[n]

    if n <= 1:
        return value

    else:
        value = fib(n - 1) + fib(n - 2)
    #    memo[n] = value

    return value


for i in range(100000):
    if i % 100 == 0:
        print(fib(i),'\n')
