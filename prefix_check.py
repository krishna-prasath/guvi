n=int(input())
a=list(map(int,input().split()))
k=int(input())
x,c,count=[],len(str(k)),0
for i in range(n):
    x.append(str(a[i])[:c])
for i in range(n):
    if x[i]==str(k):
        count+=1
print(count)
