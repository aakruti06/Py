'''Format method allows user to insert values in a string at the positions by 
using curly braces'''

'''type 1----   "{} is an integer".format(num)      '''


'''type 2---- "{0} and {1} are 2 strings".format(s1,s2) '''


'''type 3----  "{n} is a number and {s} is a string".format(n=num,s=string1) '''


'''type 4----  f"print{name} and {age} " '''


'''type 5----  f"float number.{num:3f}" '''


'''type 6----  "name is %s and age is %d" %(name,age) '''



'''------------------------type 1----------------------------------'''

a = 5
print("{} is an integer".format(a))

'''------------------------type 2----------------------------------'''

b = "python"
s = "program"
print("{0} and {1} are 2 strings".format(b,s))

'''------------------------type 3---------------------------------'''

lang = "python"
ver = 3
print("{l} is a programming language and version is {v}".format(l=lang,v=ver))

'''-------------------------type 4 --------------------------------'''

name = "sam"
surname = "t"
print(f"{name} {surname}")

'''------------------------type 5-------------------------------'''

fl = 5.5
print(f"(float number.{fl:2f})")

'''-------------------------type 6-----------------------------'''

n = "aak"
age = int(input("Enter num:"))
print("name is %s and age is %d" %(n,age))

'''--------------------------------------------------------------------------'''
