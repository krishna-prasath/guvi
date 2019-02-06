z=[]
for i in range(3):
    z.append(list(map(int,input().split())))
if z[0][0]==z[1][0]==z[2][0] or z[0][1]==z[1][1]==z[2][1]:
    print("yes")
else:
    print("no")
    
