n,a=map(int,input().split())
li=list(map(int,input().split()))
c=n-a
cl=[]
for i in range(c):
    cl.append(li[i])
print(*cl)
