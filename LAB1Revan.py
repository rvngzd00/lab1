#5
import math
eps = 0.001
s=0
y=1
a=1
while math.fabs(y)>eps:
    y=(1/(a**2))
    a+=1
    s+=y
print(s)