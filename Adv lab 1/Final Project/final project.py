#final project
#mostly copying from lab 3

import numpy as np
import matplotlib.pyplot as plt

path = "https://raw.githubusercontent.com/cchan011/Adv-lab/main/Adv%20lab%201/Final%20Project/fa23finalproj-lab2data.csv"
data = np.genfromtxt(path, delimiter=",", names=True)

millisec = data["Time"]
A0 = data["Sensor"] #output of hall sensor
A1 = data["Coil"] #analog voltage across the coil
sensorNeutral = 534 #this is the number that the sensor shows when the spring system was in equilibrium
V_sensor = A0 - sensorNeutral  #sensor output converted into voltage
V_coil = np.divide(A1, 1023) * 5 #coil voltage in volts

time = millisec/1000

fig, ax = plt.subplots(figsize = [10,5])
ax.set_xlim([0, 12.1]) 
ax.set_ylim([0, 0.5])
ax.tick_params(axis = 'y', labelcolor = 'b')
ax.set_title('Voltage across coil and signal from sensor')
ax.set_xlabel("Time (s)")
ax.set_ylabel("Voltage (V)", color = 'b')

ax2 = ax.twinx()

ax2.set_ylim([-10, 10])
ax2.set_ylabel("Sensor Signal", color = 'r')
ax2.tick_params(axis = 'y', labelcolor = 'r')

ax.plot(time,V_coil,'b', label = 'Coil') 
ax2.plot(time,V_sensor,'r', label = 'Sensor') 

fig.legend(loc = 'upper right', bbox_to_anchor = (0.90,0.87))

plt.show()

