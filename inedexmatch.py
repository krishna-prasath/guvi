a=int(input())
b=list(map(int,input().split()))
z=[]
for i in range(a):
    if b[i]==i:
        z.append(b[i])
print(*z)
