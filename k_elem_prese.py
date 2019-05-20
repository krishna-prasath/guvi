a,b=map(int,input().split())
li=[]
for i in range(a):
    li.append(list(map(int,input().split())))
z=li[0]
c=0
b=[]
for i in range(len(z)):
    c=0
    for j in range(1,len(li)):
        if z[i] in li[j]:
            c=c+1
    if c==len(li)-1:
        b.append(z[i])
b.sort()
print(*b)
