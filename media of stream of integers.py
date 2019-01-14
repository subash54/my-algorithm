a=[5,10,15,20]
a.sort()
c=len(a)//2
if len(a)%2!=0:
    print("the median is",a[len(a)//2])
elif len (a)%2==0:
    print("the median is",(a[c]+a[c-1])/2)
