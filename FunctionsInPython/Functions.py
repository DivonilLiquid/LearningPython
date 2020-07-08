#function that prints name n times
def fun(name='Divonil',n=3):   #n has been set to 3, if no explicit value from line 7 will be made. It will consider n=3.Same with name
	for i in range(n):
		print("Hello {}".format(name),"!",i+1,"time")

i=int(input("Enter number: ")) #Every variable is string by default in python. Therfore, making it integer
j=input("Enter name: ")
fun(j,i)
fun() #default parameter
