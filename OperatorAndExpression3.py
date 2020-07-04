#Bool Operator    (nor,or,and)

print("Bool Operator")
print(type(True))

print(5+True)
print(isinstance(True,int))
print(not True)
print(False or True)
print(False or False)

print(False and True)
print(True and True)


#ShortCircuiting
'''
1(A) and B = B
0(A) and B = 0(A)
1(A) or  B = 1(A)
0(A) or  B = B
'''
print("Short Circuiting")

print(1 and 20)
print(2 and 20)
print(5 or 7)
print(1 and 20)


