a=input()
j=a.split()
g=[]
print(j)
for i in range(len(j)):
    g.append(j[i][-1::-1])
print(" ".join(g))
