import math
import matplotlib.pyplot as plb
import numpy as np
import pandas as pd

# fig,axes = plb.subplots(1,3,figsize = (12,4))
# x = np.arange(1,11)

# axes[0].plot(x,np.exp(x))
# axes[0].plot(x,x * x)

# axes[1].plot(x,np.exp(x))
# axes[1].plot(x,x*x)
# axes[1].set_xlabel('x axis')
# axes[1].set_ylabel('y axis')

# axes[1].set_yscale('log')
# axes[1].xaxis.labelpad = 20

# plb.show()

# x = np.arange(1,11)
# y = np.exp(x)

# axes[0].plot(x,y)
# axes[1].plot(x,y)
# axes[1].set_xlim(1,5)
# axes[1].set_ylim(0,100)
# axes[1].set_xlabel('x axis')
# axes[1].set_ylabel('y axis')

# # plb.show()  

# fig,axes = plb.subplots(1,3,figsize = (12,4))
# x = np.linspace(-1,1,200)
# f = lambda x: x**2 + 2*x + 1
# axes[0].plot(x,f(x))

# # plb.show()

# fig = plb.figure()
# ax = fig.add_axes([0,0,1,1])
# x = np.arange(4)
# data = [[30,25,50,20],[40,23,51,17],[35,22,45,19]]
# ax.bar(x + 0.00,data[0],color = 'b',width = 0.25)
# ax.bar(x + 0.25,data[1],color = 'g',width = 0.25)
# ax.bar(x + 0.50,data[2],color = 'r',width = 0.25)
# # plb.show()

# fig = plb.figure(figsize=(10,5))
# ax = fig.add_axes([0,0,1,1])
# ax.axis('equal')
# langs = ['C','C++','Java','Python','PHP']
# students = [23,17,35,29,12]
# ax.pie(students,labels = langs,autopct = '%1.2f%%',colors = ['b','g','r','c','m'],explode = [0.1,0,0.2,0,0],shadow = True)
# plb.show()

# fig = plb.figure(figsize=(10,5))
# ax = fig.add_axes([0,0,1,1])

# grils = [25,32,34,20,25]
# boys = [25,30,19,30,22]
# grades_range = [10,20,30,40,50]
# ax.scatter(grades_range,grils,color = 'g',label = 'Grils')
# ax.scatter(grades_range,boys,color = 'b',label = 'Boys',bottom = grils)
# ax.legend(labels = ('Grils','Boys'),loc = 'upper left')
# plb.show()

# np.random.seed(42)
# df = pd.DataFrame({'X':np.random.rand(50),'Y':np.random.rand(50),'Size': np.random.rand(50)*3})
# fig = px.scatter(df,x = 'X',y = 'Y',size = 'Size',color = 'Size',title = 'Scatter Plot')
# plb.show()

fig = plb.figure(figsize=(10,5))
ax = fig.add_axes([0,0,1,1])

np.random.seed(10)

coll_1 = np.random.normal(100,10,200)
coll_2 = np.random.normal(80,30,200)
coll_3 = np.random.normal(90,20,200)
coll_4 = np.random.normal(70,25,200)

ax.boxplot([coll_1,coll_2,coll_3,coll_4])
plb.show()
