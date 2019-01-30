a=int(input())
v=list(map(int,input().split()))
for i in range(len(v)):
    for j in range(i+1,len(v)):
        if v[i]+v[j]==0:
            print(v[i],v[j])
