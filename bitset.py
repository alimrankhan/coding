
from ctypes import sizeof
from sys import int_info

#bitset #set representation

s= 0
s= s|(1<<5) | s|(1<<9)
print('{',end=' ')
for i in range(0,16):
    if s&(1<<i) :
        print(i,end=' ')
print('}')
print()
