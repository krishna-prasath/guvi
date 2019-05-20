n,a=map(int,input().split())
li=list(map(int,input().split()))
c=[]
for i in range(n):
    if li[i]<a:
        c.append(li[i])
c.sort()
print(*c)
