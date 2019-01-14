#returning index of thelargest element
a=[1,2,3,4,5]
max=0
for i in range(len(a)):
    if a[i]>a[max]:
        max=i
for j in a:
    if (2*j==a[max]):
        print(max)
else:
    print(-1)