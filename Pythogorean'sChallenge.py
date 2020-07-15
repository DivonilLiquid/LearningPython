import math
t=int(input())
while t:
	n=int(input())
	m=int(math.sqrt(n)+1)
	for a in range(m):
		for b in range(a,m):
			if a*a + b*b == n:
				print("(",a,",",b,")",end=" ")
	print("\n")
	t=t-1