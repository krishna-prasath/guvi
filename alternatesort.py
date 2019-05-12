n=int(input())
a=list(map(int,input().split()))
z=[]
a.sort(reverse=True)
if len(a)%2==0:
    for i in range(0,len(a)//2):
        z.append(a[i])
        z.append(a[-(i+1)])
else:
    for i in range(0,len(a)//2):
        z.append(a[i])
        z.append(a[-(i+1)])
    z.append(a[len(a)//2])
print(*z)
 
