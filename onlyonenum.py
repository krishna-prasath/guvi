a=int(input())
b=list(map(int,input().split()))
b.sort()
z=[]
for i in range(len(b)):
    if b[i] in b[i+1:]:
        z.append(b[i])
z,b=set(z),set(b)
print(*b.difference(z))


        
