a=int(input())
li=list(map(int,input().split()))
count=0
for i in range(a):
    for j in range(i+1,a):
        if li[i]<li[j]:
            count=count+1
print(count)                    # count
