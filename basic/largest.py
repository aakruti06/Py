''' find the largest number of 3 '''

def large(a,b,c):

	if ((a>b) and (a>c)):
		print(a)
	elif ((b>a) and (b>c)):
		print(b)
	else:
		print(c)

a = int(input("Enter a = "))
b = int(input("Enter b = "))
c = int(input("Enter c = "))
print("a = {}; b = {}; c = {}".format(a,b,c))

print()

large(a,b,c)
