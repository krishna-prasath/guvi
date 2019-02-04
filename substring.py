a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
for i in b:
    if i in a:
        c=c+1
if c>1:
    print("YES")
else:
    print("NO")
    
