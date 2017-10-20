# -*- coding: UTF-8 -*-
from functools import reduce
def prod(L):
    def gg(x,y):
        return x*y
    return reduce(gg,L)
print('3*5*7*9 =',prod([3,5,7,9]))