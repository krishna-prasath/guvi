a=int(input())
z=list(map(int,input().split()))
l=[]
for i in range(a):
    k=z[i]
    z.remove(k)
    c=1
    for j in range(len(z)):
        c=c*z[j]
    l.append(c)
    z.insert(i,k)
print(*l)
