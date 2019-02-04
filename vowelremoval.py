n=int(input())
a=input()
s=""
z=['a','e','i','o','u']
for i in range(n):
    c=0
    for j in range(len(z)):
        if a[i]==z[j]:
            c=c+1
    if c!=1:
        s=s+a[i]
print(s[::-1])
