a,b=map(int,input().split())
z=list(map(int,input().split()))
q=[]
for i in range(a):
    for j in range(i+1,a):
        if z[i]+z[j]==b:
            q.append(b)
if b in q:
    print("YES")
else:
    print("NO")
    
