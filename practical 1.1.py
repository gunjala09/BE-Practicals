#WAP a recurvsive program to calculate fabonacci number and analyze their time and space complexity
def fib(n):
    if (n<=1):
        return n
    else:
        return (fib(n-1)+fib(n-2))

n=int(input("Enter the value: "))
print("fabonacci series:")
for i in range(n):
    print(fib(i),end=" ")

