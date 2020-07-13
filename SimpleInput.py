'''
Given a list of numbers, stop processing input after the cumulative sum of all the input becomes negative.
I/P
1
2
88
-100
49

O/P
1
2
88
'''
res=0
while(res>=0):
	a=int(input())
	res+=a
	if res>=0:
		print(a)