N,A,D=map(int,input().split())
z=0
for i in range(N):
  z=z+(A+(N-1)*D)
  N=N-1
print(z)
