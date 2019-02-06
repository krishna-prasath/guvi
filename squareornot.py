x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())
x4,y4=map(int,input().split())
if x1==y1 and x3==y3 and x2==y4 and x4==y2:
    print("yes")
else:
    print("no")
