#factorial
a=int(input("enter the num"))
f=1
while(a!=0):
    f=f*a
    a-=1
print("the factorial of is",f)
#recursion factorial
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
b=int(input("enter the num"))
print(fact(b))