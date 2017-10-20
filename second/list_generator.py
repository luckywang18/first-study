# -*- coding: utf-8 -*-
def triangles(max):
    n = 1
    L = [1]
    while n <= max:
        yield L
        L = [1] + [L[n]+L[n+1] for n in range(len(L)-1)]+[1]    #n只用在for循环，for循环外无效
        n = n + 1
    return 'done'
for x in triangles(10):
    print(x)

