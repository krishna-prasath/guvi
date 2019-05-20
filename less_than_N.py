n=int(input())
li=list(map(int,input().split()))
x=[]
for i in range(n):
    if li[i]<n:
        x.append(li[i])
print(*x)
