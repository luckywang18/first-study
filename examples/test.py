# -*- coding: utf-8 -*-

def dfsdf(a):
    aa = [1];
    def triangles(p):
        return [1] + [v + p[k+1] for k, v in enumerate(p[:-1])] + [1];

    for i in range(a):
        print(aa)
        aa = triangles(aa);

dfsdf(10)

