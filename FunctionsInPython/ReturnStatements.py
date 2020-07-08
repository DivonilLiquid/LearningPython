
#return
def add(a,b):
	print(a+b)
x=int(input("Enter a: "))
y=int(input("Enter b: "))
z=add(x,y)
print(z)#Since the add function is not returning anything


def return_Add(a,b):
	return a+b
z=return_Add(x,y)
print(z)



#Try Except Finally
def divide(a,b):
	try:                     
		l=a/b
		print(l)
		return l
	except:                   
		print("Error 404")
	finally:                 
		print("Ending.......")
z=divide(x,y)
print(z)