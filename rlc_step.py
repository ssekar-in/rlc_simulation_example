# rlc circuit current, inductor and capacitor voltage - r,l and c in series with dc supply switched on at t=0


import numpy as np
import matplotlib.pyplot as plt

# define supply dc voltage, resistor,capacitor, inductor and time step
vb = 5
r = 1
c = .00001
l = .001
dt = .000001
#create empty string and append initial values
i1=[]
time1 = []
vl=[]
vc=[]
# load initial conditions to strings
i1.append(0) 
time1.append(0)
vl.append(vb)
vc.append(0)
# numerical computation, append successive step values to arrays, define end condition(number of iterations)
n=0
while (n <10000):
    time1.append(time1[n] + dt)
    i1.append(((i1[n]*(l/dt - r/2 -dt/(2*c))) +vb - vc[n])/(l/dt + r/2 + dt/(2*c)))
    vl.append(((i1[n+1]-i1[n])/dt)*l)
    vc.append(vc[n]+((((i1[n+1] + i1[n])/2)*dt)/c))
    n = n+1
plt.subplot(1,3,1)
plt.plot(time1,i1)
plt.grid()
plt.xlabel("time")
plt.ylabel("current")

plt.subplot(1,3,2)
plt.plot(time1,vl)
plt.xlabel("time")
plt.ylabel("inductor v")
plt.grid()


plt.subplot(1,3,3)
plt.plot(time1,vc)
plt.xlabel("time")
plt.ylabel("capacitor v")
plt.grid()

plt.show()

