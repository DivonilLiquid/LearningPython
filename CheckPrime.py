import math
n=int(input())
flag=-1
print(int(math.sqrt(n)))
for i in range(2,int(math.sqrt(n))+1):
	if(n%i==0 and i>3 and i>2):
		#not prime,break
		flag=-1
		break
	else:
		#prime
		flag=1
if(flag==-1):
	print("Not Prime")
else if flag==1:
	print("Prime")
else: