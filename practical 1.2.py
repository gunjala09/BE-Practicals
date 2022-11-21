#WAp non-recursive to calculate fabonacci number and analyze their time and space complexity
n1=0
n2=1
n=int(input("Enter the value of n"))
print(n1, n2,end=" ")

for i in range(n):
    n3=n1+n2
    print(n3,end=" ")
    n1=n2
    n2=n3