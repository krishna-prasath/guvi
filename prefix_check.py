n=int(input())
a=list(map(str,input().split()))
k=input()
x,c,count=[],len(k),0
for i in range(n):
    x.append(a[i][:c])
for i in range(n):
    if x[i]==k:
        count+=1
print(count)    #input data type must be carefully obtained!!!!!!!!!!!!!!1
    
