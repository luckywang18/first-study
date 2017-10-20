# -*- coding: UTF-8 -*-
import functools
max2 = functools.partial(max,6)

print(max2(7,9,8))