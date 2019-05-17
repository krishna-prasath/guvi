a=int(input())
k=list(map(int,input().split()))
x=[]
for i in range(a):
    if k[i]%2!=0 and i%2==0:
        x.append(k[i])
    elif k[i]%2==0 and i%2!=0:
        x.append(k[i])
print(*x)
