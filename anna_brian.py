a,b=map(int,input().split())
x=list(map(int,input().split()))
tot=int(input())
if sum(x)//2==tot:
    print(x[b]//2)
else:
    print("Bon Appetit")
