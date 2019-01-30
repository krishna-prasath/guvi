a=int(input())
v=list(map(int,input().split()))
for i in range(a):
    for j in range(i+1,a):
        if v[i]+v[j]==0 or v[i]+v[j]==1:
            print(v[i],v[j])
            break
# didint read the question properly
