# -*- coding: UTF-8 -*-
print(sorted([1,-4,3,-6,2,-5,100],key=abs))
print(sorted(['ad','dr','Ac','SE','Fs'],key=str.lower))
L = [('Bob',75),('Adam',90),('fADLK',80)]
def L_name(s): return s[0]
def L_score(s): return s[1]
print(sorted(L,key=L_name))
print(sorted(L,key=L_score,reverse=True))