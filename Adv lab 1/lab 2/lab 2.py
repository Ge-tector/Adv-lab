#lab 2 plot

import numpy as np
import matplotlib.pyplot as plt

path = "https://raw.githubusercontent.com/Ge-tector/Adv-lab/main/Adv%20lab%201/lab%202/data%20for%20lab%202.csv"
data = np.genfromtxt(path, delimiter=",", names=True)

millisec = data["Time"]
V_2 = data["A0"]

time = 1000*millisec
V_in = 5
R_2 = 3300

R_1 = np.divide(V_in*R_2,V_2) - R_2

R_25 = 3300
A_1 = 3.354016E-03
B_1 = 2.569850E-04
C_1 = 2.620131E-06
D_1 = 6.383091E-08

Rratio = np.divide(R_1, R_25)

T = (A_1 + (B_1*np.log(R_1 / R_25)) + (C_1*(np.log(R_1 / R_25))**2) + (D_1*(np.log(R_1 / R_25))))**(-1)

fig, ax = plt.subplots()
ax.set_xlim([0, 81]) 
ax.set_ylim([273, 333])
ax.set_title('Relation between Temperature and time')
ax.set_xlabel("Time (s)")
ax.set_ylabel("Temperature (K)")

ax.plot(time, T)

plt.show()

