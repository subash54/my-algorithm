a=[1,2,3,1,3,6,6,33,33]
b=[]
for i in a:
    if a.count(i)>1:
        b.append(i)
        a.remove(i)
print(b)
