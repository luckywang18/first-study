# -*- coding: UTF-8 -*-
def ls():
    a = 1
    while True:
        a = a + 2
        yield a
def not_divisible(n):
    return lambda x: x % n >0
def primes():
    yield 2
    it = ls()
    while True:
        n = next(it)
        yield n
        it = filter(not_divisible(n),it)
for d in primes():
    if d < 1000:
        print(d)
    else:
        break
