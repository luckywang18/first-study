# -*- coding: UTF-8 -*-
def huihui(k):
    l1 = str(k)
    l2 = str(k)[::-1]
    return l1 == l2
def is_iij(s):
    for f in s:
        huihui(f)
print(list(filter(huihui,range(1,999))))

