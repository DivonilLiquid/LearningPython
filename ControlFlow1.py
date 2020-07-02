#if elif else
a=-20
if a>0:
	print("positive")
elif a==0:
	print("zero")
else:
    print("negative")

#nested if else
b=20
if b>0:
	print("positive")
	if b%5==0:
		print("divisible by 5")
	else:
		print("not divisible by 5")
elif b==0:
	print("zero")
else:
    print("negative")


#indentation