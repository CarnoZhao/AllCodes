import time
from math import factorial
 
def factoria(N):
    N2=N
    a=list(range(1,N+1))
    while N2>1:
        N1=N2%2; N2=N2//2+N1
        for i in range(N2-N1):
            a[i]*=a[N2+i]
        a=a[0:N2]
    return a[0]
 
t=time.clock()
a=factoria(100000)
t=time.clock()-t
print (a%10000000000)
print("time: %10.5fs" % (t))