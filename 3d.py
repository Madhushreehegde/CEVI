import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7,8,9,10]
y=[212,434,622,812,120,120,140,126,180,190]
z=[289,220,430,5470,507,609,760,870,980,170]

ax=plt.axes(projection="3d")
ax.plot(x,y,z)
plt.axis(True)
plt.show()
plt.savefig("3D.png")

