import matplotlib.pyplot as plt 
import math
import numpy as np
stala1 = 1/((0.5-0.66666)*(0.5-0.75)*(1-0.5))
stala2 = 1/((0.75-0.5)*(0.75-0.66666)*(1-0.75))
stala3 = 1/((0.66666-0.5)*(0.66666-0.75)*(1-0.66666))
# initializing the list 
fi = [] 
hi = [] 
phi = []
for i in np.arange(0, 1, 0.01): 
    for j in np.arange(0, 1, 0.01): 
        for k in np.arange(0, 1, 0.01): 
             if i >j and j>k:
                   fi.append(stala1*(i-j+k))
                   hi.append(stala2*(i**(math.log(0.75,0.5))-j**(math.log(0.75,0.5))+k**(math.log(0.75,0.5))))
                   phi.append(stala3*(i**(math.log(0.66666,0.5))-j**(math.log(0.66666,0.5))+k**(math.log(0.66666,0.5))))
# plotting figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(fi, hi, phi, s = 13.2, edgecolor ='green', marker=".") 
ax.arrow(1, 0.1, 0, 0.5, length_includes_head = True, head_width=1.8, head_length=1.2)
plt.savefig("rys.png")
