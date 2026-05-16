''' bitwise operators program '''

''' & | ~ ^ >> << '''

a = 5
b = 10
#x = a&b
#y = a|b
'''
5  = 0101
10 = 1010

&  - 0000
|  = 1111

'''

print("a & b = {}".format(a&b)) # 0
print()
print("a | b = {}".format(a|b)) # 15

c = 11 # 1011
print("~c = {}".format(~c)) # 0100
print()

x = a>>1
'''
a   = 0000 0101  -  5
>>1 = 0000 0010  -  2
'''

print("x = a>>1 = {}".format(a>>1))
print()

y = b<<2
'''
b   =    0000 1010   -   10
<<2 =    0010 1000   -   40
'''

print("y = b<<2 = {}".format(y))
print()

