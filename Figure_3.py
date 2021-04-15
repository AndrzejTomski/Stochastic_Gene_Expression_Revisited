import matplotlib.pyplot as plt 
from random import randint 
from mpl_toolkits.mplot3d import Axes3D
Axes3D = Axes3D 


# initializing the list 
x = [] 
y = [] 
z = []
# setting initial conditions
x.append(1/2) 
y.append(1/2) 
z.append(1/2)
current = 0
for i in range(1, 10000): 
    
    # generating a random integer between 1 and 100 
    w = randint(1, 200)
    # appending point to the list according to selected transformation
    if w>=1 and w<=100: 
        x.append(1/2*(x[current])) 
        y.append(3/4*(y[current])) 
        z.append(2/3*(z[current]))
    else:
        x.append(24 +1/2*(x[current])) 
        y.append(48 +3/4*(y[current])) 
        z.append(-72 +2/3*(z[current])) 
    current = current + 1

# plotting figure
fig = plt.figure(figsize=(8,8), dpi=500)
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, s = 0.1, edgecolor ='black') 
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.savefig("attractor")
