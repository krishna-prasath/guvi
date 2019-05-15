a=int(input())
li=list(map(int,input().split()))
temp=0
for i in li:
    if i<0:
        temp=temp+i
print(temp)
