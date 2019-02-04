a,b=map(int,input().split())
x=list(map(int,input().split()))

for i in range(1,b):
    x.remove(max(x))
print(max(x))
