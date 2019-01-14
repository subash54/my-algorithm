a=[16,15,14,13,12,10]
leader=[]
d=0
leader.append(a[-1])
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            d=a[i]
        else:
            d=-1
            break
    if d==a[i]:
        leader.append(d)
    leader.sort()
print(leader)








