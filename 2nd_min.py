a=int(input())
d=list(map(int,input().split()))
d.remove(min(d))
print(min(d))
