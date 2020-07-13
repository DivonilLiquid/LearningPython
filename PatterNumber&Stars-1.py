'''
Take as input N, a number. Print the pattern as given in output section for corresponding input.
I/P
5
O/P
1 2 3 4 5
1 2 3 4 * 
1 2 3 * * *
1 2 * * * * *
1 * * * * * * *
'''

n=int(input())
m=n

#loop for rows
for i in range(n):
	#for numbers
	for j in range(n-i):
		print(j+1,end=" ")
	#for stars
	if(i>=1):
		for k in range(2*i-1):
			print("*",end=" ")
	print("\n")