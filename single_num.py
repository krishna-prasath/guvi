n=int(input())
a=list(map(int,input().split()))
s=set(a)
s=list(s)
z,c=0,0
for i in range(len(s)):
    c=0
    for j in range(len(a)):
        if s[i]==a[j]:
            c+=1
    if c==1:
        z=s[i]
print(z)
