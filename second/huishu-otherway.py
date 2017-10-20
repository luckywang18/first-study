# -*- coding: UTF-8 -*-
def huihui(k):
    l1 = str(k)
    a = 0
    b = len(l1)-1
    while a < len(l1):
        if l1[a] == l1[b]:
            a = a + 1
            b = b - 1
        else:
            return False
    return True
def is_iij(s):
    for f in s:
        huihui(f)
print(list(filter(huihui,range(1,999))))
#print(huihui(9249))