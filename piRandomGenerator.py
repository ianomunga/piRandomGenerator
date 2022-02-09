#Load the libraries
import numpy as np
import matplotlib.pyplot as plt

#Defining the lines of the square:
horiz = np.array(range(100))/100.0
y_1 = np.ones(100)
plt.plot(horiz , y_1, 'b')
vert = np.array(range(100))/100.0
x_1 = np.ones(100)
plt.plot(x_1 , vert, 'b')


#Plotting the random points:
import random
inside = 0
i=1
n=int(input("Enter the total number of points: "))
while (i<=n):
  x = random.random()
  y = random.random()
  if ((x**2)+(y**2))<=1:
    inside+=1
    plt.plot(x , y , 'go')
  else:
    plt.plot(x , y , 'ro')
  i+=1
pi=(4*inside)/n
print ("The value of pi is:")
print(pi)
plt.show()