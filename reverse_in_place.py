a=input()
j=a.split()
g=[]
for i in range(len(j)):
    g.append(j[i][-1::-1])
print(" ".join(g))          #wrong placement of the print statement
