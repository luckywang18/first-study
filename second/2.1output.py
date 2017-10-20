# -*- coding: utf-8 -*-
myString = 'Hello World!'
print (myString)   #直接输出Hello World!
#myString   #在交互式解释器下输出'Hello World!'
#_      #_在交互式解释器下输出最后一个表达式的值---Hello World!

# -*- coding: utf-8 -*-
print('%s is number %d!' % ('Python',1))
#import sys
#print >> sys.stderr,'Fatal error: invalid input!'   #类型错误

# -*- coding: utf-8 -*-
logfile = open('E:\log\kernel.log','a')

#在交互式解释器下输出的是对象的字符串表示，不仅仅是字符串本身
#print语句直接输出对象本身
#print语句调用str()函数显示对象，而交互式解释器调repr()函数来显示对象
