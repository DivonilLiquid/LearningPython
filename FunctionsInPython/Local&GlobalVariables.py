#Local & Global Variables
x=10

def inner():
	global x 
	x+=15
	print(x)

inner()
print(x)

del x

#Enclosures

def outer():
	x=10
	def inner():
		nonlocal x           #NonLocal
		x+=5
	    print(x)


    inner()

outer()
print(x)