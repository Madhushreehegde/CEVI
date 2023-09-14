import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7,8,9,10]
y=[2,4,6,8,10,12,14,16,18,19]
z=[10,20,30,40,50,60,70,80,90,100]

plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Sample")
plt.plot(x,y)
plt.subplot(2,2,1) #1 is which quadrant to access

plt.scatter(x,y)
plt.subplot(2,2,2) #1 is which quadrant to access
plt.xlabel("X values")
plt.ylabel("Y values")

plt.hist(x,y)
plt.subplot(2,2,3) #1 is which quadrant to access
plt.xlabel("X values")
plt.ylabel("Y values")

plt.pie(x)
plt.subplot(2,2,4) #1 is which quadrant to access
plt.xlabel("X values")
plt.ylabel("Y values")

"""plt.bar(x,y)
plt.subplot(2,2,5) #1 is which quadrant to access
plt.xlabel("X values")
plt.ylabel("Y values")
"""
#plt.show()
plt.savefig("Plot.png")

#w=plt.axex(projection="3D")
