a,b=map(str,input().split())
v,c=[],[]
z=list(map(int,input().split()))
x=list(map(int,input().split()))
v=z
for i in range(len(x)):
    v.insert(0,x[i])
    c.append(max(v))
print(*c)
