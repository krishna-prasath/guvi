n=int(input())
a=list(map(int,input().split()))
s=set(a)
s=list(s)
z=0
for i in range(len(s)):
    c=0                                   #missed the count variable
    for j in range(len(a)):
        if s[i]==a[j]:
            c+=1
    if c==1:
        z=s[i]
print(z)
