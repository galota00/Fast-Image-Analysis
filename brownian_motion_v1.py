import numpy as np
import matplotlib.pyplot as plt

# Number of computations
mean = 0
comp = 1000

diffusivity = 1e-5
def stand_dev(time):
    return np.sqrt(2 * diffusivity * time)

# Initialize coordinates and time
t = 0
x = 0
y = 0
z = 0
dt = 0.01
# Initialize corresponding arrays
t_array = np.zeros(comp + 1)
x_array = np.zeros(comp + 1)
y_array = np.zeros(comp + 1)
z_array = np.zeros(comp + 1)

fig = plt.figure()
ax = plt.axes(projection='3d')
for i in range(1, comp + 1):
    t = t + dt * i
    x = x + np.random.normal(loc=mean, scale=stand_dev(t), size=None)
    y = y + np.random.normal(loc=mean, scale=stand_dev(t), size=None)
    z = z + np.random.normal(loc=mean, scale=stand_dev(t), size=None)
    t_array[i] = t
    x_array[i] = x
    y_array[i] = y
    z_array[i] = z
    #ax.scatter(x, y, z, color=((i/comp),1,0), marker='o', s=10)

#for i in range(0, comp+1):
    #ax.plot(x_array[i:i+2], y_array[i:i+2], z_array[i:i+2], color=plt.cm.jet(255*i/comp+1))

N = len(t_array)
#ax.scatter(x_array, y_array, z_array, c = plt.cm.jet(np.linspace(0,1,N)))
for i in range(N-1):
    ax.plot(x_array[i:i+2], y_array[i:i+2], z_array[i:i+2], color=plt.cm.jet(i/N))
#ax.plot(x_array, y_array, z_array, color='black', alpha=1, linewidth=.5)

plt.show()
