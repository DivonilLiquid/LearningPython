'''
Take as input N, a number. Print the pattern as given in the input and output section.
Sample Input
7
Sample Output
 1******
 12*****
 123****
 1234***
 12345**
 123456*
 1234567
'''
n=int(input())

for i in range (n):
    #for rows
    for j in range(i+1):
        print(j+1,end="") # for numbers
    for k in range(n-i-1):
        print("*",end="")
    print("\n")