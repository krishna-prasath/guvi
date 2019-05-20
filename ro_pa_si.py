a,b=map(str,input().split())
if (a=='R' and b=='P' )or(b=='R' and a=='P'):
    print('P')
elif(a=='R' and b=='S' )or(b=='S' and a=='R'):
    print('R')
elif(a=='S' and b=='P')or(b=='S' and a=='P'):
    print('S')
else:
    print('D')          #when both player do's the same symbol
