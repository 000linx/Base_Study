import math
import pylab as plb
import numpy as np

x = np.linspace(-3,3,30)
y = x ** 2
plb.plot(x,y)
plb.show()

plb.plot(x,np.cos(x),'r--')
plb.plot(x,-np.sin(x),'g-.')
plb.show()

x = np.arange(0,math.pi*2,0.05)
y = np.sin(x)
plb.plot(x,y)

plb.title('Sin wave')
plb.xlabel('Angle',color = 'r',fontsize = '20')
plb.ylabel('Sin',color = 'b',rotation = -60)
plb.show()

y = [1,4,9,16,25,36,65]
x1 = [1,6,30,55,60,77,88]

fig = plb.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x1,y,'r--',marker = 's',markersize = 10,markeredgewidth = 5,markeredgecolor = 'green', markerfacecolor = 'yellow')
plb.show()


fig,axList = plb.subplots(2,2)
x = np.arange(1,5)

axList[0,0].plot(x,x*x)
axList[1,0].plot(x,np.exp(x))
axList[0,1].plot(x,np.sqrt(x))
axList[1,1].plot(x,np.log10(x))

plb.show()


fig = plb.figure()
x = np.arange(0,math.pi*2,0.05)

ax1 = fig.add_axes([0,0,1,1])
ax1.plot(x,np.sin(x))
ax1.set_title('sin')

ax2 = fig.add_axes([0.55,0.55,0.3,0.3])
ax2.plot(x,np.cos(x),'r')
ax2.set_title('cos')

plb.show()


fig = plb.figure()
x = np.arange(0,math.pi*2,0.05)
ax1 = fig.add_subplot(111)
ax1.plot(x,np.sin(x))
ax1.set_title('sin')


ax2 = fig.add_subplot(222,facecolor = 'y')
ax2.plot(x,np.cos(x),'g')
ax2.set_title('cos')

plb.show()

fig,axes = plb.subplots(1,3,figsize = (12,4))
x = np.arange(1,11)
axes[0].plot(x,x * x)
axes[0].grid()

axes[1].plot(x,x*x)
axes[1].grid(color = 'r',ls = '--', lw = 0.3) 

axes[2].plot(x,x * x)
axes[2].grid(color = 'r')
axes[2].set_xlabel('x axis')
axes[2].set_ylabel('y axis')

plb.show()

