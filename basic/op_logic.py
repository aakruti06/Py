''' logical operator '''

a = 5
b = 6
c = 7

print("a={},b={},c={}".format(a,b,c))


print("---------------")
print("and op")
print(a and b)
'''
truth table of and

a  b  x
0  0  0 
0  1  0
1  0  0
1  1  1
'''



print("---------------")
print("or op")
print(a or b)
'''
truth table of or

a  b  y
0  0  0
0  1  1
1  0  1
1  1  1
'''



print("---------------")
print("not op")
print(not c)
'''
truth table of not

a  z
0  1
1  0
'''

